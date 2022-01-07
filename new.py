import pyautogui
import time
import json
id_list = [
"6cb851c0a21f3ea7f1c7e27fbec4f412","25e8f3091e19c1c7393001157d727152","e718e0101fa9ece222a9b5a683ca4c9c","2ed8b584e4bd8fe81270bce8f0e5f0af","68324a0ebdca073a2938d9be8bd4cdcc","5f0b2920748ce7e3a4696719dc427635","5d97601f4a1ec4d14d0b61a23b76f6f1"
,"b1c5158754469f407edc866fb683b6e8","c48fb5d58e64aaa73c9f5c29bdc4ef7d","3813873f2a12cc62c8812acf030e2a44","e1e49c94b83f92a865c25e4402ac1a53","93cca3cf3aa41a2349bfd07deccafaf3","ff908f1a8ed6f99d7ca4590754206199","d057c7d6e236117e709f4f0dd07f4523","e12f0f60d5521a293db6bb55fb461944","c648bdc658151f69ffffd64a643e21ac","ddd5d2fef6e58347311f2e5d333724ed","bf0e5526333d34b148af1a9648bc48d2","b9b2b6637ed72f21b7ef75deffd2449d","ad392272b2778b4b137b6b09a5f59618","96af6caf64a8310033b9a6136bfd0d74","0cb2c688b9ef35940d291646c0e645ca","15a0afc24f16f65c0743befe524e4c85","f0cf47417235166433f2e4041f07c91f","8814e77a1dc8859697b023e87b9935ef","757eb56974d58fc5e679b38c2ce6b65d","773f2f8092ed6c524be00c48b0dfa013"
,"3a1d0004f82efa8e618d7a0d9ca696ec","f30af67eb95c395be7919589a2bd8049","736d3c84e91dc440549da7e792ada195","1138af2a340b3d546205181a0a7a80fe","c229dc740364baee0da92b847177933d","62a4f66bd34008284da68d4d7da73899","fcd0779cf337b435e37dca3f8af6f418","e737bf0aa9722269c19ba130bebc8a5c","88c9b96b71ffbfd3f11c9b1f222b29fa","e9f0f3c3998c0fe52fc8cc6e8c2f25b6","669d8871ccb1de7890068fab2ce5b7fa","fc71b60f102fb08c040e444be35ac6d4","b22be1b745ddd0773fd8b25a6cc7463e","f2845c981296c3aa62d38f713d0f9bcb","094b2c72b25fd719a409ea54a48a1f2d","39e85bd213b6c1ea295de2cb063a2883","0a260e7d2f3556eb01a2ad5f73ed05be","9c58211c3f8409a7d53c56465ca7e545","f25d5838195f1d9a2cbca223f7a57b46","d8acf90939cd4e67cecb6d1fd7b13bdb"
,"ba393da1ee4e7e17099c27a6692bf14f","8d95322058aad210fabf51752c4ba4a7","20380f650289d327984f83d2bfa6b6d9","235bc5e77ccb346465a0718d9274ba04","f3fbfd3801fd67e05c7650ab2286a878","dd989b239c6d1ff3e279e06ad08681e9","7e6608eb42a8477d7316dfab897c9c23","acff5a4f0f3acf88d2fec9788f40e85e","047390aab22a380ef55e95be6339be7a","acaaab99713a05b33ea6a991eddcff0a","a319d0868faa2fc4210c794fdda7ef83","21d7a430ce155cd10be64f825d2899f3","da2eda5b517926f3766681ed850e6d25","5b01cc2d71aba78a9d94508385da1bd8","b26a144e8f3a8ad6e43194325d12942c","19e4ae6f2e5fbd288f3bb2e2d604e758","925c43797812e8f22b6839a99ec2724b","90e04ad8ae02951fa58fef41e5ea9ed1","76f3ce33be89c37ce764ba7083220348","d782b3dd9497fb5147f82839329bb9bb"
,"3ee6abbda66b7ed3c57728a3343dc79e","b539b3cb8076b079e62203395cb585df","18d589b707732747320db86ef49cead3","e503e0daf23e388d48d9291b2bc42478","6abc63c93d993f598bee6deafb39b180","d4eda8b2e8bbc6cb5c0685c0b2a131f6","afc91f5d6598444a15a25bee87e98c31","52ba00eaa4bb30c718a538e66eb01d9d","00a1afa38122a1222ba26e75c3bcd890","4cc1a7b9ad860967a73bb937fe90a3a4","983eb2306e4336278a1836649c110e64","1cb743df307271cb7ff3e73a673562bc","d61413965b63cbd8362810e6fc4cc224","873666d6b19f8ae1d6e5d4fa032c00f6","bc44cc5b6b5d86d87f0c306463de1337","2cd94aad1e76ba46617f22e0002b46cc","27988cde548c58b4b28ac7260f465b14","73abed75fb29acd1156e88c4befff375","204bfe519ee50aeb7fcb3314ab51dce0","97916984a79382981e6992d521ba3c92"
,"bd8083571b690240185ae4fad5613f85","fd242280e53d901d3f44593e0a031c0a","74a641731e58770841a3f87b5b41d20c","ace18993c57c47479cacca1575fca5e4","07d9c761dcb4ff3c0bcb45f436968f4e","8f309f0e6057ad18d1477026333c9c51","e07a1aef1bd481d6bf6c596bcf58207a","c3d2387fad7803751904e732f70dbdec","9261fc2974d8ba4ad709c5982ee51796","d0c12ecd7f490ed1aa0a442a747d5160","f77789b59d760081e05cbae5487167ad","ac18d3eff7ea0c0d2ea7686bb1aa5136","4613efa94204da4356abccef4732ac5c","19e889c577ac910c039c731c41de1189","a9fc9d2b0e48b0235b9aa473e3e02531","a2a7d0fbe0a68b52770cf4a7e9352687","ed19c54f915fc7080af4ae7b7fc334ad","51ee807df09c275ad1066258af72989f","f23f684ada6af25bcc2dd8d239dbb387","a8db7988a7d5dd704a77bc92f2c636c5"
,"044cbf2cb72828341a760b881635755b","7d275a348543f628c5de66172009864b","cd7bb2e2b05d28b127f4c722b6f1b4de","3136e034c72a52dbe1bdc3280067ceba","be1df1f4a21114105809950c027072d1","4188576dc7a4ad11349563176d38adcd","14c4ad449546e36be077367b9f255ca0","274e5a5fe1dd19f12f0507e794d4d958","6f73eff3e33f11eb7888de08f80755fb","f3fd265bab66e17183d3baf6103c082c","f3b265e75e559cf16aaf911d3f217c47","57fc25037f8f63f6817657f8fa10811b","08ac57f7e61c21d970f08d4eec80ffad","d121ba0b24f03245586653294c6825d9","79a9b8127d915838c141c82654258437","07512505a0dec9ce50e23e5fb0496eea","f14ec91324d8b0ce033b84279e0eff29","5fdc245c8118af769ca62514e08edd30","cf53380d8d0c48646daf068ac8041e73","bb6acf04f1b737678c2bfa39705e5632"
,"957a0d3b5751307cd17c9727be136e1d","28f82cfb610a09f80316fbd734c815a6","e9daba12eb231f6be69bdd6882dbda2a","871e96e05423b0abc467b7badc689e85","20ad9fbd5b2433666fce4c30466386fc","3fbcb5d9ecc4562741490a452a962b4e","24a7b6c83b0b5e163f4e278a74261c9a","7d10280ee195ca05567c72c93d46a144","89a220e6215b93a0c0db2fdd6a7ebdb4","45dea9dcd58de617f6805bb48f160f7d","1492b4ed910fbe204c00c0ac4d4c3803","b60460432f897639448e1521215afa2a","b57c3aad17f72c3b64b65c13eda5d283","a72d3ce03f3e92f790e66dd4cdc9ae15","2538bfb233c9b1f13b87c055fc9a0e40","e7d26c88f541f566654ba82c6aba1250","c8e43cd4ca858cdc2adac6491dfed5f2","80ea507b7fbe3e1aec2c4e9c5b1d07be","b8f0caf22bf796e8ab302134a76be9fb","8cd5de651910ee73301390b582ebf878"]

url_list=[]
news_urls = []

print('url_list',len(id_list))
news_ids = []
for id in id_list:
    if id not in news_ids:
        news_ids.append(id)
print('news_ids:',len(news_ids))

url = 'https://buyin.jinritemai.com/dashboard/servicehall/daren-profile?uid='
for i in news_ids:
    user_url = url + i
    url_list.append(user_url)
num = 1

for n in range(0,100):
    if url_list[n] not in news_urls:
        news_urls.append(url_list[n])
        pyautogui.moveTo(x=617,y=74,duration=0.3)
        pyautogui.click(x=617,y=74,button='left')
        pyautogui.hotkey('ctrl','l')
        pyautogui.typewrite(f'{url_list[n]}')
        pyautogui.keyDown('enter')
        time.sleep(8)
        pyautogui.moveTo(x=1039,y=193,duration=0.3)
        pyautogui.click(x=1039,y=193, button='left')
        time.sleep(0.5)

        pyautogui.moveTo(x=1039,y=193,duration=0.3)
        pyautogui.click(x=1039,y=193,button='left')
        time.sleep(0.5)

        pyautogui.moveTo(x=1067,y=742,duration=0.3)
        pyautogui.click(x=1067,y=742,button='left')
        time.sleep(0.5)

        pyautogui.typewrite('document.getElementsByClassName("contact-btn")[0].click()')
        pyautogui.keyDown('enter')
        time.sleep(2)

        pyautogui.typewrite('document.getElementsByClassName("add-product-operate")[0].getElementsByTagName("button")[0].click()')
        pyautogui.keyDown('enter')
        time.sleep(0.5)

        pyautogui.moveTo(x=157,y=636,duration=0.3)
        pyautogui.click(x=157,y=636,button='left')
        time.sleep(0.5)


        pyautogui.moveTo(x=682,y=804,duration=0.3)
        pyautogui.click(x=682,y=804,button='left')
        time.sleep(0.5)

        # pyautogui.typewrite('document.getElementsByClassName("ant-checkbox")[0].getElementsByTagName("input")[0].click()')
        # pyautogui.keyDown('enter')
        # time.sleep(2)

        pyautogui.moveTo(x=790,y=973,duration=0.3)
        pyautogui.click(x=790,y=973,button='left')
        time.sleep(0.5)

        print(num)
        print(url_list[n])
        num+=1