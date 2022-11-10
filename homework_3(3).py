def characterMigration():
    dataFromUser = input('Enter smth what you want: ').upper()
    if len(dataFromUser) > 10 or len(dataFromUser) == 0:
        print('You can enter up to 10 characters!\nPlease try again.')
    elif len(dataFromUser) <= 3:
        print(f"Result: '{dataFromUser.lower()}'.")
    else:
        sliceForUpper = dataFromUser[len(dataFromUser) - 3:len(dataFromUser) + 1]
        upgradeData = dataFromUser.replace(sliceForUpper, '')
        upgradeData = upgradeData[len(upgradeData) // 2:] + sliceForUpper.lower() + upgradeData[:len(upgradeData) // 2]
        print(f"Result: '{upgradeData}'.")


characterMigration()





