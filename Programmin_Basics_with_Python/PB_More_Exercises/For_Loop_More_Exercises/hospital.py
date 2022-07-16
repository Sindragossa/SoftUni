days = int(input())
doctors = 7
treated_patients = 0
untreated_patients = 0
all_treated_patients = 0
for b in range(1, days + 1):
    patients = int(input())
    if b % 3 == 0:
        if untreated_patients > treated_patients:
            doctors += 1
    if doctors <= patients:
        all_treated_patients += doctors
        treated_patients = doctors
        untreated_patients += patients - treated_patients
    else:
        all_treated_patients += patients
        treated_patients = patients
        untreated_patients += patients - treated_patients

print(f'Treated patients: {all_treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')