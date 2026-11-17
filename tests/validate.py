import json,pathlib,re
p=pathlib.Path(__file__).resolve().parents[1]
d=json.loads((p/'itinerary.json').read_text());events=[e for day in d['days'] for e in day['events']]
assert len(d['days'])==6
assert len({e['id'] for e in events})==len(events)
assert len({e['voteKey'] for e in events})==len(events)
assert all(re.fullmatch('[a-z0-9]{1,2}',e['voteKey']) for e in events)
assert len(json.dumps({e['voteKey']:-1 for e in events},separators=(',',':')))<=300
for day in d['days']:
 previous=0
 for e in day['events']:
  if not re.fullmatch(r'\d\d:\d\d',e['start']):continue
  h,m=map(int,e['start'].split(':'));start=h*60+m
  if e['id']=='heathrow':continue # parallel airport routes
  assert start>=previous,(day['date'],e['id'],'overlap')
  if re.fullmatch(r'\d\d:\d\d',e['end']):
   h,m=map(int,e['end'].split(':'));end=h*60+m
   if end<start:end+=1440
   previous=end
print(f'PASS: 6 days, {len(events)} unique activities; vote payload <300 chars; no sequential schedule overlaps (airport routes parallel).')
