import pyautogui
import time
import pyperclip
import json
# 921.6

url_list=[]
news_urls = []

new_ids = [
'776f28389f9bb8f2649b847fa4449132', '7bf216840e23e25b641806a6fd632e4a', '43f30e8ea1629e55836222fa22dad595', 'd22ac97c8db71109a7ec5a86e6d5026a', '1b4a78a4b136e21d43c139dc04cceca6', '62bcf9e8818c1ff14e2e5a00c691767c', '878a5e85b362ec866f9ba730fe4761fd', '8634f7e0959f7d952d685d5f6ce7b1b3', 'b7ad8d18dd490e42fd04c7dbbac3b5da', '9fddd3b9d85a4e78457748f590ec6522', '8195491711440d2812a593bf22d25624', '4043202cfb0f0bc7f0290da0b3b61b2a', '2a0841dc969d5fea04c80c6d28c2a583', 'a5387a84fbf3364d72f3994e568796af', 'd6b5c40a0a86887f4d3ecdc604f9f17d', '56a2c2a016f219881a6128ee76044995', '7f71ef7619f4b109f4596702cfcd9460', 'e1c7e1f5beeb7c6467173c642186562d', '0745a0592f4da7c1c909920b014cc4b1', 'cf6ad9f2a13f5633eadf7223fad01272', 'ac9126d77c3f1e854e420d072d78b71e', '373d3e17108bf694456485088ed7fe95', '6343fdf85b3e483e41e5d73aeed52a9e', 'd9d07d627d1c495ab9bf0bc05f33db22', 'a3ba058b3188ae31538512df08ebecd3', '38370fd9a1d086ad87800e962a1225f2', 'a158e813dd48f5282c83a22dfbed3454', '915f9d887ac46cbb2bf5b222d15cd127', '87323b23b7c4e476d697a235438d8f66', '1118adb553ec04cb12830c0ec27da714', '4db2ecccc0438805651c028770717fae', '9fef5aa58a7461af84e243970d30ce3f', '7a888eb844a27bc9884ce9fe9ae2d149', '466bd252606323de1bc55befef60e9a2', '687b2f23d16ee432a5819078b046e98e', '5db6873cd559d47811ad3aa5f25f86d1', '091d92ef31e8dd1336d538fbfd47141f', '68429ca57f3fd01da77da32258584fe0', '6503b24454f63a13f72f34bf526c0742', '61fc70f1a4f37d44ffce798755fc49af', '3adbb222c920db3c9f6b53e59bc2846d', '2ca4f3139b497336efe9f228b67dc94d', 'f39fd67e9c2a4ff62fb14ab29f4aa728', '751879318286a6ca07e0ac70a6e2e853', '8f5cfe4f6069ae85903a3047c94a88ea', 'dbb6ef22791c28f9057cd7056decbf4b', '8680e1e5df08089b1b9e7a229de630f9', 'edf03c6341e70dce695f92f7239cc2a6', '440b485f08dd3217e0199d0b029d12cd', '9c9b47ff1bb3afc97737924321082739', 'e96a3bf6488f0b0826a77746ccfa1d09', '11779865956c145cb564f188f5bfeaad', '070de8ba2cf748938b0af2b8e0aec049', '85f6689267043f639a823f1f027c4e6d', 'cbd5de81b7abc4dd7c8ca8973ff6d857', '2699196edd6e5f6605fad43b97efdc19', '94462d738190120d03195e5ee1111fc4', '7472d8aac3885d33cec682ddbfd3ff9d', 'ee06d7903e5e329b645dabc007f04e01', 'af72b26f9a8722efb62d8b0d24e6413e', '9060204dac026df395e87c556e0c6989', '38305e0e1e94892e155ccbd039ea55aa', 'a31100ecda6b5f69664d0e42a5ed18ff', 'a75c000689d9ee58482932feb1127c5e', '170adc641145bd1d123b971c5fc22a4f', '311bfde40c0a9967a04da56602084353', '6f95029bc4fd476ba9bcf78966238a99', '47de38762ea3732cf58b83e0b930e51b', 'f02138d457a5c4f93ae278f0f2169378', 'f422673a7cef2151aa620a2ca3d24bcd', '6ebf9907441d5ec8492a59ac60248c2d', 'c2b3dc5e2c5b02bd49670f7154beab62', 'fe599cd0cbc2fc132a4705ed5a0e0227', 'bd3dc8bcd46fabd6ddceecbca58a1e0b', '60835ccaf30817a9068ff4a83c033151', '425f5d0810c00318e357dd976012f7d5', 'f9f7a7eea141dac550353e1abd07d454', '47303a55be70da1cfdf455e5603dd089', 'a2f7d368fb8da4e524ab6024315ecd16', 'd325663c6c2e4160631adfe3ce21dd1a', '563deabb33763981cb1b721d5310ee15', '977d965deab7fc14937299f75a1793a4', 'b89cfba2ded9ea41d62b453397b158a0', 'd2c5a62b5fec58dd834ffc1ea2396e3e', '3c39cf946715bb73d7c40e8b17330712', '7e41523835f571f6c4fe03d33f839293', 'c79e4a3a76130707a7ba54c588b5a128', 'a6700a3b0e946be5a6e844ae53f86e9f', '0d2bdbe38c86bd3d7e859ff26c12947b', '6a5d83ead3e303b42b1e602420466bfd', 'fc252e0a0ed4204e1cb4133e12223f0c', '0f06b01b88189c965613f0cf407a92ca', '455430d676e11e832c8e9cf52fda1687', 'bc7542df13f7214d7bab0d8be9b08d0a', '0b82020266acda0cbf8ab0eb6b062ce1', 'd0d001c68db7d922d274da920a0bb3f1', '61257deef828a4193bfb735f09aee50f', '7649506d1cde696164171353d42b819f', '32adc2ee53a45218e3758e5d71bfe00d', '5aaf1ffc24fe67f8f9420f4209d6f587', '144799b97ccf3f494463a9f298fed65e', 'a2fefc98af1db5349c78f7a95ef70823', '9d6cbbcb61f13ae5c9a113517a46df6a', 'b6de91494afb5ba85bbc310166a8ec49', '6b9165adacf3502eb6d71ac18e666645', 'b9ff00775252718866b3a7bfda6f81a0', 'a48a8693ae942f9c4b0bdb0880b8d21e', 'b60dbf487f42c7cc4d7a203be32a8686', '021d01c6d0229f5e7ace4a2505ec7afd', '789b8ef1a1318e3e96e859b3629ff6c9', '95e0a634e679ecf9978a13ae1234f2fc', 'b3259bde2e6cce278a1f3c71208273a9', '0587ab1091fbc6c21ab7e9452847e8c6', 'a20f15c4591f6201a43a33c14193c247', '3f212cbf7706a535d823e72982175f43', '0f366f9e9435fe6aefd88bb3e8c417ee', 'c81f5e84eb86f63a6025a082d94f9933', 'b07b5b31841173748af59df2ac426a16', 'b633e500a41f59d91b47554e09714438', '031614f38d1343edba10672d4b7542e1', 'd813325b9e25fec477c53b1a84f6c909', '80e397d5613b869d6f3195dc86f7fe6c', '4a89c8d0a66287cb4d8ee92564da36a1', '720fa9c767befd77e9f98cdbc4a1995f', 'c34128f1a3f193950bce04dc41b786b0', '1f063a7f575ce476ef9ead99925fc098', 'e5c9298744e57d9df16b49a67a00b8fd', 'f3f3d131ed8f22bff23306a0b6b685e3', '8b69b5cdfb13deefc65b1f6908760cd6', 'ae56b4494eed606b3ad7be7a495435aa', '01f53d4ee45a41ef83be9bbe9c82188c', 'a43146af2dd8fd532512433443c5c9e6', 'f696589491797048f7c472cdf5c0cb25', '5f3866683067c7471b4c54f009070e9f', '8023cef2a53f45ff9afb94a3bce3f185', '32a27721abfda725e9e9d95cb70bcf3b', 'b745eddf3edbad489071813b893598f1', '58d5f471afe991600e0a400c33896f2e', 'e47a791775dee16296a3e37d690c55d3', 'a7634535fe0bd504fee1e20f064175ec', '1079f90098283e937095d9a77fdce276', '46a1689b9dd9fed91f26156b6e350a6a', 'bf73c71dce90f7432eecbbf777bbcb16', '1d1a0e56c52c1d094bd06a2140d166f0', '41c50d28cd2416c89f13b0cabb968832', 'c29427350e767b68e5f991fce8dbd7de', '65ae0675860792613f29ce7580f4902f', '4a4aae2801c550bf6804f054eb5f156a', '5575b18526aa557c5206ebeb57a86de8', 'e2c9b33890b1ad836fe9ed3c625164cf', 'e40384f8ab9f441f5760a9c7867ea899', 'c19c01d9b11f0850be17e4fe392096a1', '24c09c2a412d741e02987732004984b2', '72d5cab3572a785753d386281d69ca00', 'ff3bf5aff5603c087d072a79bafcf9cd', '7b749dc591bb33892ccd99af3a109329', '50578aabd7cf2e9aac2cf91616ff070b', '659f4b8b9eb6a2dc33671b5b1477e1f8', '9c43f1cb9ced8fa129dcc8cb1872c9fd', 'ab493a0cd1d4f695b78e577a1ce2d83f', '0ff9ab4fa470281df05b444d9f05836d', '00a2f230932a2474b943bc3419cbfcad', 'f43df58b8a6f0190cac89fb59fd6f103', 'd94a8a16a50c1d7227d140eb1a4630b7', '90efca44e1000ae45e65f69ec2e3ab7f', '65f7cbbd14dea5acc9b79dd5f55ec2cc', '01a4e472c1db1cc969b219eaddaf756b', '9c710804a4999f2b7b10f85402e3be49', 'b819eea912f98b6cfd1509bbeb40dcc0', 'e0e86ad85f7a40f33727f433c4da12d1', '5beaa9679de41b96ac116a35583f01a1', '62a4f66bd34008284da68d4d7da73899', '446e8216ce93ce1deed58286abd7c205', '591839d776b06174271e6eeedd736908', '9106e8a77ef1530b0f2f6de5fc6e49a7', 'e312db959a58536060f1c764a8913f83', '9cb5d9c7c6c22a7cde8f9a4215d8285a', '87cd78daa0bd43aba40fe63f02a5a61d', 'c8da946df149c6c17ce6916b5e8867bc', '9d225f04e504dcd62115a7e02a4fe524', 'f5aa6e93bcfacc2be1c4497f66c0c608', 'b3321779dfd5ac2ac8ec1223e4bfea65', 'e8943580ef53c03644b3bd3aaf930e11', '9b10b482ff280c8d8912ee1512178f98', '1d7365d23541f8bde0294d396f6c0831', 'f1fda4b7cabe11ee5d23ed592e1b9be8', '76396f631460a1986e255a7a9522cf29', '605ca3f3988ee4a5c14f370c2368ea60', '1bc99c8bce48fe81dc2b1e2058371455', 'b4f01de15da057945fbfc44c233645bb', '0d4962aa4609a99b0760956b1f5950cb', '04df2410678274791d94b443dd8f262b', '1b254a2ce8ffd0fad9dfb39b4bbc84a9', '9c98b7cdcc8eab735f76031120931e39', 'f3b1625a90b43bbe30d7ed8b5e04a63d', '4f6a5108bde65bb0ec01e00480adceab', 'e15f53c97a2ca69a6abe3d07f29d6944', 'a69f9b6dfaf1ec3f17bd99b203531735', '3a3680b27d166ad9b6c8f68316bd177c', '6ae29928e8a8158d6aef026bafee3880', '76b6737ae414468cb8d615672f57ad93', '3443d5a1efb2a1e866743217a1157df0', 'b26bdb0d99ba977fd8b338cd36b10c3d', 'ca21653f6bcfe486eaf28505746da85c', '71050c4c1a9aed3499f145f0775b045d', 'f98b78b9e6a2a20f59d8f8f9485585c2', 'a5ead5d7812409e24309b1bd2af28ff5', '2438496ffda65b426eccd59815806f74', 'e1f3ce7bb70fc05d44cfcfbf5a80993e', '5742858d58f5c7b18bbaaaf9b53b248c', 'cc364ce621ce8efc4eaa481f5c75e42d', 'c39997203976346267abcd58f4b98160', 'a10c11bb60cab554f1c30b99d2e908bb', '01f8dfc78ceeb911e09cd2aefc2ed874', '5ca8c9841009cff7be6918ebf4fc6f4d', '71661b8e8b95cf99d2218fa9081dfcd4', 'b72336bf670227f9937b852428f20270', 'b28052231b1152a68a9267fbc66f1448', '76aab3c2bdcc2b15a6adbb70200b52c6', 'e1005b42817579f58d7bce97bf3d3410', '5e641aa9298afdb4859b7c52ab3ab55e', '9be77151e5e50220c25a1a62953a4ed6', 'c085c7ce2b2d74d28685d86fa49cf3d7', '96359a319535bf470c474a1764e0ba0b', '8a9fcf2fbde916ccf7f138f688710db3', 'c6123bd3b57b47132f553805e19b7839', '02cc477098e00d6060018a7de463e8fb', '7da332f56513c8318de7ae04eabb845e', '2891065e8de9ee2b866e494dfa18d0e4', '6d48ebd4ef564f0ced9fa8894322264a', '62ff936ca04fbd23d6bd35b42dae0f1e', '79e00b88e7f2975e3436b610753c5efa', '473ee6c10895370df02e54976bc897c3', '17483cfca83f53d67674f610a7142184', '6f46ec8d03bcdd687f0f1c9b5154f192', 'd9fe50d5eb47bfdaf902aff3a03f5fd1', '7d166ea5ab0f715a927172812682e1f0', '86bfcfd068a7895dbd3e9673fe81c433', '3f1ea0166fb3aca622b278420b9b7f82', 'a438431428b7129b5d1982535aa3c311', '8c821e49515ac5339aa6a3c952913946', '88f06bb148b49f09146274f8eb9b80e3', '76e8b3d45ed2ffa61d75d3ccc1b5bc68', 'd07d8d8bc6839850be18d0bb50d0b205', '4243dd16df4f6a8f870eb17844de2103', '1eacf07e27f50356dddc294ed7ad9a99', '9b50e49a08fb150ce11e93e72891d3c2', '74d9dcf6b47846f561fce0f942f537da', '4ff9159293b0cb7a2a08d683fdbb02ae', 'f6b153749e6e97f3df70dacd889ea821', '677b0023122ec2f7b7c954f89497ffc8', '3f8221a53765c983ac8cc97c90305a51', 'aae9622e44ba38f7e8415554cfe7a992', '2d01982b2fcbb9904db449cce9e6a824', 'dd3833c24ebc10de0a9d687b0996c11e', 'b41e70a706e01def7af367f91e28e966', '8f457e6c9b4f932020427369ccd003a7', '313bfe036a68ed58d4a47a0c7e04dc2e', '237c6145eefc3d0b983f8e63ceab0535', '97b12a47619fb72151656bfcbec741ed', '3156ad335b7073568ab4734cc5b1707e', '0f28c8ca83f3b7999bb4241c2cc162ec', '45b1a563174a708de3cd020ae3ee8f9e', '6fd2301cffacd2b03fef0bbf8d3cab9d', '8f448b096836df3387d7a709ecdb9caf', '7bacde0c7403a784b71e2a5002ca6a7b', '749298f1c2026bfe2729949017ef7fdc', '6ad16bacfae69afe451a35524421cd2b', '450723a2324abf982d7f000111d6a306', 'a609e22b1df2f4f9b97a85160710b949', 'fd242778e41ebdb6e1be74333a32aaa3', 'f06a2d9a3a68d6e5cea4887fd25d1610', '5b919de3c58499ec8999af3b0824705f', '02aa14bea7928ad6f123667398199807', '24ec91f895efd69520569f496503816c', '86128b958f0b5e7a3f3da096159b2ec4', 'feac19f02c67f59f30b40d02be956cfb', 'dee392efe0dee69ddaedebaeb17b9d0e', '3e5135ec08042c0bbb84b5363d34c58a', '7eb61f880848a5bb91dbc7ae19fe0e5d', 'c366cf01e0581693c2aeb63e8a6a96ef', 'b805d023caa264ee02a168e5e88914c0', 'dcf09fe906f937629e682b22bfa40db4', '0dd1c569d814cc51d313b041421b4acb', 'fe7792f769ffa9bfba9f2f05b1033215', '4fa6100546abfc417e03b7a969cfb86d', '3aced8ac306794285dc64a8d99256755', '9cb08487ff104401c2a175648252a25d', '7c2d982c289dd362ae8b2d874a025f38', '18a82579629f3846a55afe57ba58a7a3', '4ea977b0127c5b5f4f237fab8eabe2f2', '005f5853baf3d4f969b078ba09bd1f95', 'f8f5ff33c3f464920b6dd0a3ba6e3871', '7932d07d5dda1ad482ac3520032ca0cb', '59a0eea803d264361c2dde6cec71b910', 'd171f5423c76e3314e7a1aeae8c82f71', '445f048bf67df7f549942cb0c87f49f5', 'f083046437649c928d09e2ad9e477b01', '0cf4ce271e5b61f81db7daa2bb25353c', '11230a52262ddcb006066bc5742b83c2', '125f1475a181588548878b227a740bb2', '288bb5de4b4f3afef350a697e3076a49', '463cfac540a7e74f229317352b5733b9', '5b7cb8df2d4efdde62ad415be5a4e25f', 'f89c6aa1617dfe52220b9e3adcf57de6', '030e15bff1e63116644842f85812249f', '38a2d285b630f4a360e8f7c8aec9828e', 'ff2beece46349759f6df5fea8e9d2e6c', '11186bdda0f918f741df6a4fa7394db0', '180cc7482bdd84814439a37642a8ecd9', 'a1b624538a52fee85abbfe4a4dd21bfd', '11bed31dfe157cd5cda5ad60daf35f3f', '07dd2702db272dcb478763f61339b5e7', '0eaccd4287369bc8bd91a5a96f8f6027', 'b169eefdb10fadea63aa683dcb7c77f4', '0e7b0ab7fb6f941c534ca2b0698d8f78', 'a32d7a6012c2172a1103c74976027c8a', 'a08c8e9cf096f0242a4185dce08eb959', 'bc6fffbb2cb66061fb37daf43197be20', '9083fdf6b7540ad5f51caf3d2078bd61', 'c864ea4c5614e4d9222f198be32d6d91', '4d832d95a7e14da282e3e583972564fd', '8cebc1493e8b5ea245c5dd0efd0d90e4', '3d3c497a17974710470bc1330df264f6', '4c2d76b82fd7401c5ef9d3d3931fa228', '15ccabd79cacb4949226f5ef55f026b3', 'ce7d2a82b5db75fd5683b632567db968', '5e6ff54cd6bc80be2c1b37b2505cab6c', '49703041d74d940660a61af3a963d80c', 'f78e4ebac69c8c43ca7f9f838c8ba3f2', 'dd4bc38cb6971a0b22a263d7d4106ab6', '7ae9b2fddf26a34d2bd39842d920c3e2', '758a4ecf85da6562ce550d6289e6e701', 'ae3e2d3ed6e9dd0d997ec1910e302767', '506f74496c032c0bb35e4f3ea180534d', '460d87df0c30ba9bc3a60d563716ca0d', 'e97b5d2c1b613cf1f77da877607db12a', '781feda4f45abf147e4aac961ecf50a0', '22d3164bb59604ea44e7e4c9dc6d403e', '72e01145644a1534a84eb4f8617eb13b', '84fdfa1d5986f5292be58135e6ee11ed', '388ec8826efca9d23cbeb1dc2fe6a281']

'''for id in id_list:
    if id not in news_ids:
        news_ids.append(id)

print('news_ids:',len(news_ids))
print(news_ids)'''

def pyautogui_action(action):
    if action["name"] in ["move_to_click"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')

    elif action["name"] in ["select_all_and_copy"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "c")

    elif action["name"] in ["select_all_and_paste"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "v")

    elif action["name"] in ["select_all_and_copy_and_paste"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        write_content = action.get("content","")
        pyperclip.copy(write_content)
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press('enter')

    elif action["name"] in ["open_console"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("f12")
    print(action.get("action_name"))
    action_sleep = action.get("sleep",0)
    time.sleep(action_sleep)


print('new_ids:',len(new_ids))
url = 'https://buyin.jinritemai.com/dashboard/servicehall/daren-profile?uid='
for i in new_ids:
    user_url = url + i
    url_list.append(user_url)
num = 1

action_item_click_list=[

]

for n in range(0,100):
    if url_list[n] not in news_urls:
        news_urls.append(url_list[n])
        pyautogui.moveTo(x=617,y=74,duration=0.3)
        pyautogui.click(x=617,y=74,button='left')
        pyautogui.hotkey('ctrl','l')
        # pyautogui.typewrite(f'{url_list[n]}')
        pyperclip.copy('%s'%(url_list[n]))
        pyautogui.hotkey('ctrl','v')

        pyautogui.keyDown('enter')
        time.sleep(8)

        pyautogui.moveTo(x=1209,y=178,duration=0.3)
        pyautogui.click(x=1209,y=178, button='left')
        pyautogui.moveTo(x=1209,y=178,duration=0.3)
        pyautogui.click(x=1209,y=178,button='left')
        pyautogui.moveTo(x=1324,y=819,duration=0.3)
        pyautogui.click(x=1324,y=819,button='left')

        pyperclip.copy('document.getElementsByClassName("contact-btn")[0].click()')
        pyautogui.hotkey('ctrl','v')
        pyautogui.keyDown('enter')
        time.sleep(2)

        pyperclip.copy('document.getElementsByClassName("add-product-operate")[0].getElementsByTagName("button")[0].click()')
        pyautogui.hotkey('ctrl','v')
        pyautogui.keyDown('enter')
        time.sleep(0.5)

        pyautogui.moveTo(x=431,y=346,duration=0.3)
        pyautogui.click(x=431,y=346,button='left')
        time.sleep(0.5)
        pyperclip.copy('3526488155261953561')
        pyautogui.hotkey('ctrl','v')

        pyautogui.moveTo(x=242,y=529,duration=0.3)
        pyautogui.click(x=242,y=529,button='left')

        # pyperclip.copy('document.getElementsByClassName("ant-table-cell ant-table-selection-column")[0].getElementsByTagName("span")[1].click()')
        # pyautogui.hotkey('ctrl','v')
        # pyautogui.keyDown('enter')
        # time.sleep(0.5)

        pyautogui.moveTo(x=783,y=796,duration=0.3)
        pyautogui.click(x=783,y=796,button='left')


        pyautogui.moveTo(x=962,y=984,duration=0.3)
        pyautogui.click(x=962,y=984,button='left')
        time.sleep(3)

        print(num)
        print(url_list[n])
        num+=1