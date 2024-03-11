- [x] визначити предметну область
  > "Діагностика несправностей комп'ютерів"
- [ ] побудувати словник предметної області
- [ ] намалювати семантичну мережу

#### Словник предметної області

#### Семантична мережа

- Dont turn on
  - PSU failure
- Turn on but no screen
  - GPU failure
- Blue screen
  - OS crash
- Program crash
  - Software App crash
- Program wont open
  - Software App crash
- Program wont update
  - Software App crash
- OS wont update
  - OS crash
- No internet
  - Cable damage
- Making noise
  - Fan failure
- Freezing / Working slow
  - CPU failure
- hardware failure
- software failure

---

patient has either symptom or diagnosis.
symptoms splits into three - body temperature, pain place, pain type.
temperature can be either normal or high.
pain place can be either stomach or back.
pain type can be either mild or severe.
if pain place is stomach, diagnosis includes apendicitis.
if pain is in back diagnosis includes piolophrenitus.
if temperature is normal, diagnosis includes chronic apendicitis or chronic piolophrenitus.
if temperature is high, diagnosis includes severe apendicitis or severe piolophrenitus.
if pain is mild, diagnosis includes chronic apendicitis or chronic piolophrenitus.
if pain is severe, diagnosis includes severe apendicitis or severe piolophrenitus.
an arrow goes from patient to diagnosis and then splits into those four types of diagnosis - chronic apendicitis, chronic piolophrenitus, severe apendicitis, severe piolophrenitus.
diagnosises like apendicitis and piolophrenitus split into their specific types.

---

client has troubles and problem.
troubles splits into three - does turn on, does make sound, does freeze.
