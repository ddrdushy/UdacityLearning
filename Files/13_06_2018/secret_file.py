import os

def rename_files():
    # get the files from directory
    file_list = os.listdir(r'.\\prank\\')

    current_path=os.getcwd()
    os.chdir(r'.\\prank\\')

    # for each file rename the file
    transalate_table=str.maketrans("0123456789","          ","0123456789")
    for file in file_list:
        print("old file name is: {}".format(file))
        print("new file name is: {}".format(file.translate(transalate_table)))
        os.rename(file,file.translate(transalate_table))

    os.chdir(current_path)
rename_files()

# output
"""
old file name is: 16los angeles.jpg
new file name is: los angeles.jpg
old file name is: 17cairo.jpg
new file name is: cairo.jpg
old file name is: 22rochester.jpg
new file name is: rochester.jpg
old file name is: 25madrid.jpg
new file name is: madrid.jpg
old file name is: 28houston.jpg
new file name is: houston.jpg
old file name is: 29bristol.jpg
new file name is: bristol.jpg
old file name is: 29buenos aires.jpg
new file name is: buenos aires.jpg
old file name is: 2chennai.jpg
new file name is: chennai.jpg
old file name is: 2hyderabad.jpg
new file name is: hyderabad.jpg
old file name is: 35miami.jpg
new file name is: miami.jpg
old file name is: 36sydney.jpg
new file name is: sydney.jpg
old file name is: 37athens.jpg
new file name is: athens.jpg
old file name is: 41seoul.jpg
new file name is: seoul.jpg
old file name is: 45austin.jpg
new file name is: austin.jpg
old file name is: 45ithaca.jpg
new file name is: ithaca.jpg
old file name is: 46colombo.jpg
new file name is: colombo.jpg
old file name is: 47london.jpg
new file name is: london.jpg
old file name is: 47sao paulo.jpg
new file name is: sao paulo.jpg
old file name is: 47singapore.jpg
new file name is: singapore.jpg
old file name is: 48sunnyvale.jpg
new file name is: sunnyvale.jpg
old file name is: 4istanbul.jpg
new file name is: istanbul.jpg
old file name is: 50san diego.jpg
new file name is: san diego.jpg
old file name is: 52new york.jpg
new file name is: new york.jpg
old file name is: 54dallas.jpg
new file name is: dallas.jpg
old file name is: 55kiev.jpg
new file name is: kiev.jpg
old file name is: 5bogota.jpg
new file name is: bogota.jpg
old file name is: 61edinbrugh.jpg
new file name is: edinbrugh.jpg
old file name is: 64seattle.jpg
new file name is: seattle.jpg
old file name is: 66san jose.jpg
new file name is: san jose.jpg
old file name is: 68pune.jpg
new file name is: pune.jpg
old file name is: 69chicago.jpg
new file name is: chicago.jpg
old file name is: 69shanghai.jpg
new file name is: shanghai.jpg
old file name is: 72bangalore.jpg
new file name is: bangalore.jpg
old file name is: 72bucharest.jpg
new file name is: bucharest.jpg
old file name is: 73delhi.jpg
new file name is: delhi.jpg
old file name is: 74tel aviv.jpg
new file name is: tel aviv.jpg
old file name is: 83gainesville.jpg
new file name is: gainesville.jpg
old file name is: 88jacksonville.jpg
new file name is: jacksonville.jpg
old file name is: 89berkeley.jpg
new file name is: berkeley.jpg
old file name is: 90beijing.jpg
new file name is: beijing.jpg
old file name is: 93manchester.jpg
new file name is: manchester.jpg
old file name is: 96karachi.jpg
new file name is: karachi.jpg
old file name is: 97oakland.jpg
new file name is: oakland.jpg
old file name is: 9barcelona.jpg
new file name is: barcelona.jpg
"""