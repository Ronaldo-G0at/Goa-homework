#საკლასო დავალება: შექმენით ფუნქცია სახელად manual_range, რომელსაც გადაეცემა სამი პარამეტრი (start, end, step).
#ფუნქციის დავალებაა რომ გადაცემული პარამეტრებით შეადგინოს დიაპაზონი, შე
#მდეგ ამ დიაპაზონს გადავუაროთ ციკლით და დავბეჭდოთ მხოლოდ ლუწი რიცხვები.
#ფუნქციის გამოძახებისას მას აუცილებლად უნდა გადაეცეს 3 არგუმენტი.
#ფუნქცია გამოიძახეთ მინიმუმ 5-ჯერ სხვადასხვა არგუმენტებით

def manual_range(start, end, step):
    for i in range(start, end, step):
        if i % 2 ==0:
            print(i)


            manual_range(2,10,8)
            manual_range(28,12,412)
            manual_range(10,20,40)
            manual_range(22,44,84)
            manual_range(54,7,776)