import androidhelper

droid = androidhelper.Android()

message = droid.dialogGetInput('speak','hello sir i am jarvish what can i do for you').result

droid.ttsSpeak(message)
