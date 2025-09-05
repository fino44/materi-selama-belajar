import csv

print("---csv aja ---")
file_path_csv = r"C:\Users\ThinkPad\OneDrive\Dokumen\python\uang jajan.csv"

with open (file_path_csv, "r")as file_new:
    next(file_new)
    read = csv.reader(file_new)
    list_read = list(read)

    
    print("semua data")
    print("-" * 20)
    for baris in list_read:
        no = baris[0],
        nama = [1],
        uang = [2],
        jajan  = [3]

print(f"| {baris [0]} | {baris [1]} | {baris [2]} |")

#tambah data
with open(file_path_csv, "a", newline="")as new_file:
    write = csv.writer(new_file)
    write.writerow(["1", "fino", "18"])