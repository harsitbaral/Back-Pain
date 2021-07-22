from win10toast import ToastNotifier

notifier = ToastNotifier()

title = "Time for a break!"
message = "You've been on the computer for 30 minutes! It's time to get up!"
path = "exercise.ico"

notifier.show_toast(title, message, icon_path=path)