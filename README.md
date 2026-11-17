# London & Oxford

Static, mobile-friendly itinerary for 17–22 November 2026. No build step or third-party frontend dependencies.

## Editing

Edit `itinerary.json`. Each activity has a permanent `id` and `voteKey`: **never change or reuse an existing voteKey** when reordering or deleting activities. New activities require an unused one- or two-character lowercase alphanumeric voteKey. Votes follow the activity, not its time or day. All votes for one person must fit KeyVal's 300-character value limit. There are currently 28 activities; a full set of vetoes occupies 197 characters.

Times and travel are human-authored planning allowances, not verified rail departures. Booking links do not imply a reservation. Re-check actual availability, closures and engineering works before booking. Sunday airport activities run in parallel for separate travellers.

## Shared voting

Open `https://dgondos.github.io/london-november-2026/#vote=TOKEN` with a cryptographically random 32-character base64url token, shared privately. Never commit the token. The browser remembers it in localStorage. Choose a name; click Like or Veto, and click again to clear. Four small separate records in KeyVal avoid different people overwriting one shared document. Updates perform read-modify-write then read back to confirm. Two devices simultaneously voting as the same person are not transactionally protected; use one device per person at a time.

The app uses KeyVal POST `/get` and `/set`. Anyone holding the token can read/change any person's votes. There is no identity authentication, retention guarantee or service SLA. The itinerary and source code are public. Votes are not encrypted at the storage provider. The UI disables writing when it cannot verify storage, and never reports an unverified write as saved. Voting links use URL fragments and referrer-policy `no-referrer`; no analytics or external script dependencies.

## Run

`python3 -m http.server 8765` and open localhost:8765. `node --check calendar.js` checks JavaScript syntax. `python3 tests/validate.py` checks activity identifiers, voting size and clock intervals. GitHub Pages deploys the repository root from main (no build).

## Hungarian calendar UI and weather

`calendar.js` renders a proportional single-day calendar (132 px/hour) with a detail dialog. Hungarian copy lives in the data file and UI. Technical notes stay in this README, not on the travel page. Wednesday is shopping/Shard; Saturday is Westminster/Eye. Existing vote keys remain unchanged.

`weather.json` is a real hourly Open-Meteo snapshot for London and Oxford, including source retrieval time. The browser attempts a fresh forecast on load, falling back to the snapshot. Activity forecasts aggregate the relevant location and hours, including the next day for after-midnight events; the displayed rain percentage is the maximum hourly probability, not a whole-interval probability. API variables: temperature_2m, precipitation_probability, precipitation, weather_code, wind_speed_10m. No invented or climatological fallback values. After the trip falls outside the forecast window the saved snapshot is retained. API times are Europe/London; the trip takes place entirely in GMT, which permits the UTC parsing used here. If reusing in British Summer Time, replace that parsing with proper timezone handling.

The weather refresh never silently moves bookings or changes the schedule. Current scheduling puts Wednesday's drizzle during shopping, Saturday's drier hours outdoors, and Oxford's outdoor walk before dusk, followed by the college and dinner. Changing forecasts may require a manual itinerary edit. Preserve transit buffers when rearranging blocks; Sunday airport blocks are parallel.

