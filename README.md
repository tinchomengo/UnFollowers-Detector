![readme_image](https://user-images.githubusercontent.com/64234011/230240974-509f49fd-4ec5-4d87-9b57-e43563bc6ad5.png)

# Instagram UnFollowers-Detector

Given the information you can download from Instagram, this program allows you to navigate to the required files, and detect the unfollowers you follow.
Accesing your instagram data requires the following steps (they can be done from Mobile or Web):

Instagram > More > Your Activity > Download Your Information > HTML or JSON (the program supports both) > Send

After receiving the zip file via mail, be sure to extract all files in any folder

After that, execute the _detectorbytincho.py_ file and then you will be able to navigate the folder where you stored the extracted zip file

The 2 files that are needed inside the extracted file, are stored in the following folder:

_Extracted Folder Name_ > _followers_and_following_

After opening the _followers_and_following_ folder the 2 files needed are "followers" and "following" (they might be .html or .json, depending on the format you requested)

* _Note 1: It is crucial that both files are in the same format (either both .html or both .json)._

* _Note 2: In the last step before send, if you download your info from iOS or Android, it doesn't require for you to choose the format and by default sends it as HTML (as far as I know)._

* _Note 3: The "followers" file might be named "followers_1", so you can select it from the file browser is it only matters its content, and not its name._
