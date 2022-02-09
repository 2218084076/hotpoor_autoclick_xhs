import pyautogui
import time
import pyperclip

# 打开审查元素位置 921.6
# 2022/01/15
urls=['http://www.dianping.com/shop/k369DGLgKua0OJ6q', 'http://www.dianping.com/shop/k5opqS1j5LHT5EqS', 'http://www.dianping.com/shop/kamcclC66syYOQzJ', 'http://www.dianping.com/shop/lakUrEgo2Ce6ntuX', 'http://www.dianping.com/shop/G6xVnzM837PyDaJV', 'http://www.dianping.com/shop/l61MXCEN6ZFiHS4O', 'http://www.dianping.com/shop/l2ZJ8WMOspCpoXwa', 'http://www.dianping.com/shop/H5jmPCBlPPJw3dFw', 'http://www.dianping.com/shop/l70rk16tYXiPnXHK', 'http://www.dianping.com/shop/Ha4bkV6mJ9YYIrcf', 'http://www.dianping.com/shop/k1qH0TpE74Ta0bBa', 'http://www.dianping.com/shop/H50EJ168XfpkRsbE', 'http://www.dianping.com/shop/G1vuT4codjTAnoZx', 'http://www.dianping.com/shop/H1vMx1BYGeZlndCu', 'http://www.dianping.com/shop/H17mMyWgaC9aUXKt','http://www.dianping.com/shop/G3Z0coPd7xD6hMH8', 'http://www.dianping.com/shop/laQK4rMfwLbLRtQJ', 'http://www.dianping.com/shop/l9adqiEd9WmRYPii', 'http://www.dianping.com/shop/G2vOzWqalzbPFuVH', 'http://www.dianping.com/shop/H72rPXpkJQWS8Ncw', 'http://www.dianping.com/shop/k7LVR8oHX6y9KeF8', 'http://www.dianping.com/shop/G1A756QGCqa03KS1', 'http://www.dianping.com/shop/l40wCC57KUoKnopu', 'http://www.dianping.com/shop/G85uTxqN0XLGCUqM', 'http://www.dianping.com/shop/l4YI6GlsTa3EHYZM', 'http://www.dianping.com/shop/H49hDu50ANT5OFEs', 'http://www.dianping.com/shop/H5X6kFQVnvJK2ZoS', 'http://www.dianping.com/shop/l1jTClRh9LwVIVuE', 'http://www.dianping.com/shop/H7htZCfu0vDrUV8i', 'http://www.dianping.com/shop/laStemBlFPGNfDaq','http://www.dianping.com/shop/k4RvSsBjBz7v3r7q', 'http://www.dianping.com/shop/k6fnUtWwCba14H7N', 'http://www.dianping.com/shop/H3jGSBl2JEm6GtxC', 'http://www.dianping.com/shop/l8ez9Eaupvmhv9IQ', 'http://www.dianping.com/shop/jV3YIk1Z9jWMCAAq', 'http://www.dianping.com/shop/l5pRyzU1FfPH81zD', 'http://www.dianping.com/shop/k9vCJCcCIPLmxD5T', 'http://www.dianping.com/shop/k2GkUq0YKjds1WVC', 'http://www.dianping.com/shop/H30432oWADfI6EK0', 'http://www.dianping.com/shop/k6vLRrz3zcqZyMdq', 'http://www.dianping.com/shop/l3SwvvPxcZCfrRjL', 'http://www.dianping.com/shop/k9dKBr6bZrsjFi7B', 'http://www.dianping.com/shop/H8UB76kS2UBtOaDw', 'http://www.dianping.com/shop/H5kdnuErLcfMuxgW', 'http://www.dianping.com/shop/l345CNcnVY6h4iu8','http://www.dianping.com/shop/G7k4wl8TaBWAVyFH', 'http://www.dianping.com/shop/GaaAOEsoVoJD0ycM', 'http://www.dianping.com/shop/l8vKvBkyvbzwcUmc', 'http://www.dianping.com/shop/G2PEOltCHaYqNaAC', 'http://www.dianping.com/shop/G25Sk5rd6H4c0NFo', 'http://www.dianping.com/shop/G2PE01IxilXrXWUP', 'http://www.dianping.com/shop/H8ItXq6y8cjG3497', 'http://www.dianping.com/shop/G5bs86MOozXPl1xP', 'http://www.dianping.com/shop/l6UU2wDLIP9OZz8I', 'http://www.dianping.com/shop/jK8pccTrVFWn6lbg', 'http://www.dianping.com/shop/l4ebOzLrh4p4J8nL', 'http://www.dianping.com/shop/G7oLVVfYCjkciKaK', 'http://www.dianping.com/shop/G4LHk7yqt29P5ciR', 'http://www.dianping.com/shop/k7kujJwBfoHcD4kt', 'http://www.dianping.com/shop/HaWj47RdAq9z9ABQ','http://www.dianping.com/shop/H50Bwr3HPHUic5BR', 'http://www.dianping.com/shop/G2a3GbvBo84SsgLy', 'http://www.dianping.com/shop/l34HuucnOGydHgv3', 'http://www.dianping.com/shop/H337YTpfHi4K9lHW', 'http://www.dianping.com/shop/k5gsznDeufayoSNs', 'http://www.dianping.com/shop/l6y7PLYXvLitxarR', 'http://www.dianping.com/shop/k8FFDqKJ8Dil5wNr', 'http://www.dianping.com/shop/k4kEhGu4qNDBQRca', 'http://www.dianping.com/shop/l3TqSEi4Y70hUuVW', 'http://www.dianping.com/shop/H3qGPagGTojcJLOE', 'http://www.dianping.com/shop/H2kPoS6EqUHltDcD', 'http://www.dianping.com/shop/k8V82WA2E94jIaoG', 'http://www.dianping.com/shop/G2fhUSk0oake1FDI', 'http://www.dianping.com/shop/EdNrLgmlGdIrERka', 'http://www.dianping.com/shop/l6sdPLjxuGy9aLkT','http://www.dianping.com/shop/G8IiziyN1V0vRbQs', 'http://www.dianping.com/shop/H2gUlYrdnpsGNWxk', 'http://www.dianping.com/shop/H64mTLILMKoJxcMp', 'http://www.dianping.com/shop/G7Bn6tJmhZRThaNW', 'http://www.dianping.com/shop/k5s3uTOpcmyeGtOF', 'http://www.dianping.com/shop/l213oKIBvFHDxKfU', 'http://www.dianping.com/shop/k6L7KsAbotqYhM4X', 'http://www.dianping.com/shop/kacNdbkZk6JtYRgq', 'http://www.dianping.com/shop/G6AjrBiQ1wpv4O85', 'http://www.dianping.com/shop/G6gAlHkVgTO6dFC0', 'http://www.dianping.com/shop/H4fOCK6uJNd6VrlK', 'http://www.dianping.com/shop/G847yIb3dQKQAo2Z', 'http://www.dianping.com/shop/G5vDaXTn1MxjVCED', 'http://www.dianping.com/shop/l4Nq64XqwJUTl96w', 'http://www.dianping.com/shop/k2VWLq02NL588jHK','http://www.dianping.com/shop/H6xxDaZDLOSRS9ds', 'http://www.dianping.com/shop/G1pouO8rjkvzrpRG', 'http://www.dianping.com/shop/iNHtvmuiXxe6QPAl', 'http://www.dianping.com/shop/H8a9G9Bb8VkJjFJa', 'http://www.dianping.com/shop/G39p7CuZHjSqFaDO', 'http://www.dianping.com/shop/HaZ1fmV5nZakwlbN', 'http://www.dianping.com/shop/H9PJ5G1t34SdKLee', 'http://www.dianping.com/shop/Ezb4DphQ54h5KTpe', 'http://www.dianping.com/shop/G6SJFurfcrCwAAlq', 'http://www.dianping.com/shop/k8w0z1iRSO8xv6wl', 'http://www.dianping.com/shop/k5gHWc5CIvnw9KQG', 'http://www.dianping.com/shop/Hajg3WJmqbXGH3Lo', 'http://www.dianping.com/shop/k8N1qwU9bVDg3eJu', 'http://www.dianping.com/shop/H2icLVNdXuSm5DUd', 'http://www.dianping.com/shop/l5NRPi0iOpg0Ccop','http://www.dianping.com/shop/H8k1QhcEpvUmo673', 'http://www.dianping.com/shop/H2CmT5KuI1QSG8Ev', 'http://www.dianping.com/shop/H1I1gfAp678bfRl7', 'http://www.dianping.com/shop/iRaidDHPos2fXOQR', 'http://www.dianping.com/shop/G66NnHxQ8HCNOvik', 'http://www.dianping.com/shop/l36T6O7gv4gHsuUi', 'http://www.dianping.com/shop/k7Dr67FgLQW8qGHz', 'http://www.dianping.com/shop/H9tWYnBsfTYFrciW', 'http://www.dianping.com/shop/k9uACptMmCpQj0Lo', 'http://www.dianping.com/shop/kaX52KgqhkN5bgtA', 'http://www.dianping.com/shop/l9XHIVB74iUJUDbd', 'http://www.dianping.com/shop/k1c1Gpu5XyfKromF', 'http://www.dianping.com/shop/i51tYrxeRQD7foAo', 'http://www.dianping.com/shop/G2FVz414VQQwKPtS', 'http://www.dianping.com/shop/FB6nclYfFf79oOVo'
,'http://www.dianping.com/shop/H8VnH8MzvUhqo5uz', 'http://www.dianping.com/shop/k6meUkGfPU4LoQ1U', 'http://www.dianping.com/shop/G9vfJEUQOORSG4Dy', 'http://www.dianping.com/shop/k4I4buYR4eZJzOMy', 'http://www.dianping.com/shop/j5GIXwn4Mfpefq16', 'http://www.dianping.com/shop/G4ekGLFFoc1XnDDA', 'http://www.dianping.com/shop/H4odQZSoprTjnN18', 'http://www.dianping.com/shop/l4nPdBD0eH9VOlrh', 'http://www.dianping.com/shop/k98dwQpleHfa27nH', 'http://www.dianping.com/shop/l4cy17LCPfmD1ECh', 'http://www.dianping.com/shop/G8HSzQm6yKPf7yuZ', 'http://www.dianping.com/shop/H9BaHqknnoQIjxFh', 'http://www.dianping.com/shop/l6kXi9mSLcnsKi3j', 'http://www.dianping.com/shop/l80KZO6uhc5WPaEa', 'http://www.dianping.com/shop/H2E2ho9UmNtY75Ky','http://www.dianping.com/shop/G9V3l7X2MRhBVHHH', 'http://www.dianping.com/shop/H87QppQyNkr2BZ0T', 'http://www.dianping.com/shop/l1kNb7g57OVLNtfj', 'http://www.dianping.com/shop/l7wK4JWIVAcxtuIk', 'http://www.dianping.com/shop/G7a5Brvus8whXijV', 'http://www.dianping.com/shop/H2bqBxrGFoPmzdFn', 'http://www.dianping.com/shop/H4rplwSAWMV0j3Bc', 'http://www.dianping.com/shop/H5xN4626vKYp5NBs', 'http://www.dianping.com/shop/G7pUWJzwDXf01648', 'http://www.dianping.com/shop/H77hbotimi1YHEDu', 'http://www.dianping.com/shop/l3r7GfuhImbuVCZt', 'http://www.dianping.com/shop/k36X1XZq9QmD2irG', 'http://www.dianping.com/shop/H5W8HLRkH1d4sAVx', 'http://www.dianping.com/shop/G2qcctzqJwJUpckd', 'http://www.dianping.com/shop/l5D7xrDu6AWYOVUj'
,'http://www.dianping.com/shop/l6IGBlzg3Od54lzl', 'http://www.dianping.com/shop/k90kNun2wUAioMBZ', 'http://www.dianping.com/shop/G4NwH7bcYTpPW1Cv', 'http://www.dianping.com/shop/H7DIMKxBZaeDvQZR', 'http://www.dianping.com/shop/l95XDEd96K32B2k9', 'http://www.dianping.com/shop/H2BZG7QPW6tOkYGc', 'http://www.dianping.com/shop/H1899CoYnPfSKfox', 'http://www.dianping.com/shop/l8XsdfchOmGySimS', 'http://www.dianping.com/shop/k9Gx0JfdpL5YDsCl', 'http://www.dianping.com/shop/H9dDht2rJUIbwE54', 'http://www.dianping.com/shop/H3UPtvxOt8SdQqQJ', 'http://www.dianping.com/shop/k8feRvs7PbnvnyUl', 'http://www.dianping.com/shop/H9yurL3LkT7csXdJ', 'http://www.dianping.com/shop/k7thnu4H6kTPtEdg', 'http://www.dianping.com/shop/H3fohC9ZuXTBRG2M','http://www.dianping.com/shop/G77Rx8xaAGEX5to6', 'http://www.dianping.com/shop/k8rYXZ51B7fXLsiA', 'http://www.dianping.com/shop/H22JmVfE9suX2Nbp', 'http://www.dianping.com/shop/k5rw6yKKdOs7JE38', 'http://www.dianping.com/shop/kaM95n6PtB30jOQ5', 'http://www.dianping.com/shop/l14MLt3qRvezCLkH', 'http://www.dianping.com/shop/l9gxn9jbPxdYSrIY', 'http://www.dianping.com/shop/G7u72f6SMTnBqwfL', 'http://www.dianping.com/shop/H2DmBBZNsNbUWBOd', 'http://www.dianping.com/shop/k4wrpoFsmeEJbGE0', 'http://www.dianping.com/shop/k29m7fDG9jAM1JJF', 'http://www.dianping.com/shop/GaiYROM7GzVHawie', 'http://www.dianping.com/shop/H6yM8FIpa2wDsodh', 'http://www.dianping.com/shop/l7zIkRPF868YAnTB', 'http://www.dianping.com/shop/H8KEfyZDmnQAbv5H'
,'http://www.dianping.com/shop/k9t3QSAWN4lBEJPJ', 'http://www.dianping.com/shop/k9kc9KVvXVZRLnAw', 'http://www.dianping.com/shop/l5FdQL309oDajK0M', 'http://www.dianping.com/shop/G1yoLU24PP6SmXBA', 'http://www.dianping.com/shop/k3LlBlbptJpFJgkt', 'http://www.dianping.com/shop/H8GloRI9lu79QBB3', 'http://www.dianping.com/shop/H21S5z99BwzwRumA', 'http://www.dianping.com/shop/H8KoOruGN3OfzN6M', 'http://www.dianping.com/shop/FxeohOl0tP4QGJX5', 'http://www.dianping.com/shop/l2I3LPRxDjPBnzIO', 'http://www.dianping.com/shop/H3ldxCnz4oVa81lP', 'http://www.dianping.com/shop/l7PmezWCO3cWH89w', 'http://www.dianping.com/shop/k8bWnzBNamYrtEMq', 'http://www.dianping.com/shop/G9EKwp767gVOMxi0', 'http://www.dianping.com/shop/la882imbsUuWFfZv','http://www.dianping.com/shop/l5MGyf0beJIbOWDV', 'http://www.dianping.com/shop/H2Y8RPJweLKbPN6l', 'http://www.dianping.com/shop/l5ayaGf4TdY5Oton', 'http://www.dianping.com/shop/k1UCG14GPvNRUUrm', 'http://www.dianping.com/shop/k9oGm7qoUTIAX6Qi', 'http://www.dianping.com/shop/G65TPQLAnqKXZC5d', 'http://www.dianping.com/shop/k41suVBYeJcoCCjV', 'http://www.dianping.com/shop/H8YNccM28ilSascQ', 'http://www.dianping.com/shop/H2vqlX4O14HVzFVU', 'http://www.dianping.com/shop/lapJhTBi0eMmk3ar','http://www.dianping.com/shop/G8X0ePfN5ANh1nK2', 'http://www.dianping.com/shop/GamImp96AmQNpbW9', 'http://www.dianping.com/shop/iqsrWvTIhS1aZqwz', 'http://www.dianping.com/shop/k5YZGxUEd6K7WHgr', 'http://www.dianping.com/shop/G33oSZ7vNCsxaWjw', 'http://www.dianping.com/shop/k6U7JOEAQn5rRPUy', 'http://www.dianping.com/shop/k3U7JVZF2QEi5iQ4', 'http://www.dianping.com/shop/k8TObsuwzywyDUCv', 'http://www.dianping.com/shop/l1MK56oh6bEbTNWS', 'http://www.dianping.com/shop/k75ET0Bnt0ZrJxiJ', 'http://www.dianping.com/shop/H69yrP5t7kDkX1HI', 'http://www.dianping.com/shop/l2B1dtV60Iuwwo1i', 'http://www.dianping.com/shop/k1D2Re3zQNT1JN6k', 'http://www.dianping.com/shop/Hav8AJWHIlRjCdWO', 'http://www.dianping.com/shop/HaX0YDcbDyJUt3hE','http://www.dianping.com/shop/Hav8AJWHIlRjCdWO', 'http://www.dianping.com/shop/k75ET0Bnt0ZrJxiJ', 'http://www.dianping.com/shop/HaX0YDcbDyJUt3hE', 'http://www.dianping.com/shop/H2jXZzxD6UQo4hnp', 'http://www.dianping.com/shop/l1hXLmRPUeRqMLZJ', 'http://www.dianping.com/shop/GafBQkfx6MYIui5H', 'http://www.dianping.com/shop/FX2Wcle3MEGOphpA', 'http://www.dianping.com/shop/H6eGgOJB3raMg8uQ', 'http://www.dianping.com/shop/G5IYZqtHYafC5777', 'http://www.dianping.com/shop/FLCPOh6xDRRMiuA8', 'http://www.dianping.com/shop/G9kK3TJJostiXn03', 'http://www.dianping.com/shop/G1SO4iWmokt8hv10', 'http://www.dianping.com/shop/l7u4knHfV0uVnhqx', 'http://www.dianping.com/shop/k7WUKhTArpt2R0uz', 'http://www.dianping.com/shop/H3S1ndzAAGGUkiS2'
,'http://www.dianping.com/shop/k83OdvMwtwpkolCV', 'http://www.dianping.com/shop/H52ywFl7orGhdrVl', 'http://www.dianping.com/shop/l5wQjtMX0fG1nEHb', 'http://www.dianping.com/shop/H5I5k4sIyLsVBkIT', 'http://www.dianping.com/shop/G2VmDBJkwEJe9i9S', 'http://www.dianping.com/shop/H8Krop6r0Ru3cRE2', 'http://www.dianping.com/shop/HaQiGcllcUIn3dns', 'http://www.dianping.com/shop/G6KCVVnnkxQRx54e', 'http://www.dianping.com/shop/k7v3QawnrUkohwGP', 'http://www.dianping.com/shop/H3fJ6xVjTf7NIh0E', 'http://www.dianping.com/shop/l8Z1iUSR5IskQMVC', 'http://www.dianping.com/shop/H4DZ54A66EFTcOai', 'http://www.dianping.com/shop/H5lo7tD3m9TPjT1D', 'http://www.dianping.com/shop/l8ehPAwe2mLkwjvv', 'http://www.dianping.com/shop/H1WT7cWspHo6V5Wp','http://www.dianping.com/shop/H4DZ54A66EFTcOai', 'http://www.dianping.com/shop/H5lo7tD3m9TPjT1D', 'http://www.dianping.com/shop/l3EaDfruqXoEc1aD', 'http://www.dianping.com/shop/H504guckIkBxKo0d', 'http://www.dianping.com/shop/H8CcaAIe1xdsdfNa', 'http://www.dianping.com/shop/k3WhTnxuCafpCJct', 'http://www.dianping.com/shop/GahTlxVPUNL9guXT', 'http://www.dianping.com/shop/G55FyCY2UhyuVB5J', 'http://www.dianping.com/shop/kalpKjI4cK51qv6J', 'http://www.dianping.com/shop/G7NInHoz02R4tpHk', 'http://www.dianping.com/shop/k8kSQB7oEmqRIJ8Z', 'http://www.dianping.com/shop/iXMnB6aB5vnfVs6w', 'http://www.dianping.com/shop/G499pADMgQqyMCCS', 'http://www.dianping.com/shop/k9sgtBqVdzaylT55', 'http://www.dianping.com/shop/G9rMCuWrtMSCZde9'
,'http://www.dianping.com/shop/k3b2dwwnAqmDzFjC', 'http://www.dianping.com/shop/H4r4hkdF2eYVeH1Z', 'http://www.dianping.com/shop/G6awACcxnQzrNKvo', 'http://www.dianping.com/shop/H9Hxu4KvpVn8dMRL', 'http://www.dianping.com/shop/G9rMCuWrtMSCZde9', 'http://www.dianping.com/shop/l6A9QOErDlVkVSFl', 'http://www.dianping.com/shop/k4pp2tSUHl1KMcRv', 'http://www.dianping.com/shop/l6PXdyAglOgszbaf', 'http://www.dianping.com/shop/l84BhG19Xd3vO8oU', 'http://www.dianping.com/shop/iIvuddW76daGJ7Vh', 'http://www.dianping.com/shop/k3izZh638pQm4fOc', 'http://www.dianping.com/shop/l2rHjRS7zN956LvU', 'http://www.dianping.com/shop/H1QxPKVPGbseLNBK', 'http://www.dianping.com/shop/l3xP2z69x4CAX0RI', 'http://www.dianping.com/shop/j2ed0Sa0YazdFBFC','http://www.dianping.com/shop/k8yriwfo6mLVqcER', 'http://www.dianping.com/shop/GaSOLVVww7g0K3lU', 'http://www.dianping.com/shop/G766G9CEPnretnlU', 'http://www.dianping.com/shop/Hay6jihV9WGH1LVx', 'http://www.dianping.com/shop/l1YIKxip63pBiTUD', 'http://www.dianping.com/shop/G4imW3Wb3GZr3uyz', 'http://www.dianping.com/shop/G13Wch4GhIQsYt79', 'http://www.dianping.com/shop/k3NL9vtYC1nWZSFi', 'http://www.dianping.com/shop/k497tExHFnJEArmV', 'http://www.dianping.com/shop/G4gbqlSdPiKapZ3k', 'http://www.dianping.com/shop/iQ7i6ScncN1f9iTn', 'http://www.dianping.com/shop/G8qXuq0dM5uXBqcg', 'http://www.dianping.com/shop/l7a9F9GrveD5GvKd', 'http://www.dianping.com/shop/kaR2aNrgppZrTWY3', 'http://www.dianping.com/shop/H9vHNirBE7gVmAzI'
,'http://www.dianping.com/shop/G13Wch4GhIQsYt79', 'http://www.dianping.com/shop/k3NL9vtYC1nWZSFi', 'http://www.dianping.com/shop/k4pp2tSUHl1KMcRv', 'http://www.dianping.com/shop/G4gbqlSdPiKapZ3k', 'http://www.dianping.com/shop/GaSOLVVww7g0K3lU', 'http://www.dianping.com/shop/l7a9F9GrveD5GvKd', 'http://www.dianping.com/shop/G8qXuq0dM5uXBqcg', 'http://www.dianping.com/shop/Hapt1o0EeSpCVsub', 'http://www.dianping.com/shop/G3z9wcaVyA25t8k3', 'http://www.dianping.com/shop/l3XbWYPFrudGGtxS', 'http://www.dianping.com/shop/k497tExHFnJEArmV', 'http://www.dianping.com/shop/k1GwJYeHQsZ2HHtf', 'http://www.dianping.com/shop/G9HRPzkd6Jese2ql', 'http://www.dianping.com/shop/H8pOhTyZCu8C6R03', 'http://www.dianping.com/shop/GaYueDlDbjtaRoVR','http://www.dianping.com/shop/l8LLZUFSmei0Xmla', 'http://www.dianping.com/shop/kakt48pNdxwXjHJW', 'http://www.dianping.com/shop/k2r602v5sHqlKHKn', 'http://www.dianping.com/shop/j1PjgENExsieq5BE', 'http://www.dianping.com/shop/k497tExHFnJEArmV', 'http://www.dianping.com/shop/Hapt1o0EeSpCVsub', 'http://www.dianping.com/shop/H8EGTUcZZFamIsq3', 'http://www.dianping.com/shop/GafmkSkSqtQ0MP3m', 'http://www.dianping.com/shop/l8KlRJ16CT8hVdJR', 'http://www.dianping.com/shop/H5PmjNRQ9OBd3IZJ', 'http://www.dianping.com/shop/G9v22U5xCmCDHFCV', 'http://www.dianping.com/shop/k7wcuQykdrvFqitL', 'http://www.dianping.com/shop/k6C20lKcyihXcI5r', 'http://www.dianping.com/shop/G9vkX7Q7SGxnflkA', 'http://www.dianping.com/shop/kaDngir6t3R4Blbu'
,'http://www.dianping.com/shop/HafX2dmE3OgQ9DAF', 'http://www.dianping.com/shop/k9WGNkNnJpn0MERs', 'http://www.dianping.com/shop/iML1m7QNXl7NJft9', 'http://www.dianping.com/shop/l2Mgqr2qTlvIisw9', 'http://www.dianping.com/shop/H442ep6d5vBQ5E8E', 'http://www.dianping.com/shop/l5EuvNs2h9BUB3jQ', 'http://www.dianping.com/shop/Hapt1o0EeSpCVsub', 'http://www.dianping.com/shop/Hag66KLBit6mYFD1', 'http://www.dianping.com/shop/H3AQet8pkyTu1zdc', 'http://www.dianping.com/shop/G7dtzQuocTMvS9EP', 'http://www.dianping.com/shop/G9xEj7Cx2NmrY8AP', 'http://www.dianping.com/shop/EqXZy719JpMjhx2L', 'http://www.dianping.com/shop/G9vkX7Q7SGxnflkA', 'http://www.dianping.com/shop/l9Im9aGLwb9jMm1z', 'http://www.dianping.com/shop/k2hjtzi082wgBQC3','http://www.dianping.com/shop/iYKLDfHiFpLvGI6E', 'http://www.dianping.com/shop/EgvwAG4CvG10rPpw', 'http://www.dianping.com/shop/HakRooTu3Pn6569g', 'http://www.dianping.com/shop/l7iOWQDIRdYj5A7X', 'http://www.dianping.com/shop/G8fkWqdIsahhw7My', 'http://www.dianping.com/shop/l5sqHy6LEEzvOL6c', 'http://www.dianping.com/shop/l51Hw19GzHwRIHd3', 'http://www.dianping.com/shop/E2PVmOJnmWgbKgi6', 'http://www.dianping.com/shop/k7sEcSK5c2lipDdq', 'http://www.dianping.com/shop/G2ArDH2ysP1Wt5XP', 'http://www.dianping.com/shop/jm7VA1DqQ70XzHcz', 'http://www.dianping.com/shop/l1rNj7eG4OXAPmFg', 'http://www.dianping.com/shop/G1eYqqetHCKWh9oh','http://www.dianping.com/shop/k7v3QawnrUkohwGP', 'http://www.dianping.com/shop/k9FiOPSMA5j5z8xi', 'http://www.dianping.com/shop/k1z6St5fRJkzmTjL', 'http://www.dianping.com/shop/H6JtStOkI8ZqS37K', 'http://www.dianping.com/shop/H27GbGRcVIN6ZqK4', 'http://www.dianping.com/shop/E9Cazp2mq02kIIWn', 'http://www.dianping.com/shop/H1cWIOcAuKEBURIy', 'http://www.dianping.com/shop/H8s2RvO9FGLrzE64', 'http://www.dianping.com/shop/FJxdmt9HQ5JHApT8', 'http://www.dianping.com/shop/k8MmQQONzS9NA45E', 'http://www.dianping.com/shop/l8WStnBM23c4dXoK', 'http://www.dianping.com/shop/H442ep6d5vBQ5E8E', 'http://www.dianping.com/shop/H6q6KojZAsvvFODV', 'http://www.dianping.com/shop/l9DjhVymkYhfXSaR', 'http://www.dianping.com/shop/k3MKAOKgHh9iIcSv','http://www.dianping.com/shop/G2iwVyf2vPCbO4Z7', 'http://www.dianping.com/shop/H8eagpneW0BL9H8L', 'http://www.dianping.com/shop/H7PuulTzSpTYMFu9', 'http://www.dianping.com/shop/H9g0HxZliRnfGUjU', 'http://www.dianping.com/shop/k6kAdel5dKChIXzi', 'http://www.dianping.com/shop/k8yriwfo6mLVqcER', 'http://www.dianping.com/shop/G93TpHdsQG3u0KVx', 'http://www.dianping.com/shop/G7FT2tQ32wMcoB9e', 'http://www.dianping.com/shop/H1CZp9zcZVFtovet', 'http://www.dianping.com/shop/l8a0aoH4fIp2tiXF', 'http://www.dianping.com/shop/H3NNRqZ7cR3mYsNw', 'http://www.dianping.com/shop/G2U5Egd8NgYnpVML', 'http://www.dianping.com/shop/H3S1ndzAAGGUkiS2', 'http://www.dianping.com/shop/k2hjtzi082wgBQC3'
,'http://www.dianping.com/shop/k6xR6JKMxyyYmxzl', 'http://www.dianping.com/shop/G6KCVVnnkxQRx54e', 'http://www.dianping.com/shop/l3oDvPXhMPoz4dN3', 'http://www.dianping.com/shop/H7Yiw2ewcmX42XvJ', 'http://www.dianping.com/shop/HaCSEnDZpFQeZTPt', 'http://www.dianping.com/shop/k83OdvMwtwpkolCV', 'http://www.dianping.com/shop/l4TMPzVQLJFBqG3X', 'http://www.dianping.com/shop/k5onDOpUPNcGXkap', 'http://www.dianping.com/shop/l4mBxrj5PfxiUOhx', 'http://www.dianping.com/shop/l9sNNACjMyHeMLAM', 'http://www.dianping.com/shop/l22DYnE4l7ytzCqf', 'http://www.dianping.com/shop/k92WIoWtvIy17Rwo', 'http://www.dianping.com/shop/jhFnLx9V7aIvfgpc', 'http://www.dianping.com/shop/H49dR5nEc6Ylw448','http://www.dianping.com/shop/GaewuPwFe8sFbw88', 'http://www.dianping.com/shop/HaO70y386lf3cuSB', 'http://www.dianping.com/shop/k6Tis8puuevwX5K9', 'http://www.dianping.com/shop/G46nzsbP096DE2LW', 'http://www.dianping.com/shop/l2syIvmhMGW4EnIO', 'http://www.dianping.com/shop/k889Z6Y2dl0ZF9Rl', 'http://www.dianping.com/shop/G5ZfIQMyjOMInKLP', 'http://www.dianping.com/shop/l5CCseZVUwtRSJ7E', 'http://www.dianping.com/shop/H5bHDkL38m3DvH4z', 'http://www.dianping.com/shop/HaQiGcllcUIn3dns', 'http://www.dianping.com/shop/k4Pu9Uj8zVlalo89', 'http://www.dianping.com/shop/G4uf9uBckCYwZV6F', 'http://www.dianping.com/shop/G8crMdNn4AlA7fhJ', 'http://www.dianping.com/shop/G3z9wcaVyA25t8k3', 'http://www.dianping.com/shop/k4yXPsjHUzmwDSdm','http://www.dianping.com/shop/Ejg1r7CZXVJaJy1H', 'http://www.dianping.com/shop/kapsAXXf0CJeRWq9', 'http://www.dianping.com/shop/FAajLKqBQzsZTCCJ', 'http://www.dianping.com/shop/H5P8bzORpjuEgNjx', 'http://www.dianping.com/shop/H3y41M8EDgnEB7SC', 'http://www.dianping.com/shop/H34Cof7saLhLTavQ', 'http://www.dianping.com/shop/HaxFS2yo1OEhSLzQ', 'http://www.dianping.com/shop/Haz9krGiKcXEIC4r', 'http://www.dianping.com/shop/l9sYcPRTI0sKCMMW', 'http://www.dianping.com/shop/l1YIKxip63pBiTUD', 'http://www.dianping.com/shop/k1jS97iGD3ulWyRx', 'http://www.dianping.com/shop/k7wcuQykdrvFqitL', 'http://www.dianping.com/shop/HaFfN8vI5V5pmmrX', 'http://www.dianping.com/shop/H5X9a0jDVM1cIygJ','http://www.dianping.com/shop/l2YY3ggXtNJ7U4hd', 'http://www.dianping.com/shop/G8mXLPAf5tbw9mhF', 'http://www.dianping.com/shop/k2WGXIy0uOIdL4LV', 'http://www.dianping.com/shop/k9gOqMMuWXxZXUcT', 'http://www.dianping.com/shop/k3B4JOVrFEIHefmC', 'http://www.dianping.com/shop/G4nVZBrXH91Q8QLm', 'http://www.dianping.com/shop/l9Im9aGLwb9jMm1z', 'http://www.dianping.com/shop/k8uuSUBCU1LQgTJ1', 'http://www.dianping.com/shop/G6ZPNiBRkM6iIcsC', 'http://www.dianping.com/shop/ka1Xbukj3zR3nXc1', 'http://www.dianping.com/shop/l3XbWYPFrudGGtxS', 'http://www.dianping.com/shop/H6ke087sNT4PYZTz', 'http://www.dianping.com/shop/HaQkGjUPBEpRpvN1', 'http://www.dianping.com/shop/k7o2FpCN7EvubjPl'
,'http://www.dianping.com/shop/k4JDT0Tvz2mdbYkO', 'http://www.dianping.com/shop/l2RjVVdVSaG1ayAn', 'http://www.dianping.com/shop/k5ys3E0JEfw5zdad', 'http://www.dianping.com/shop/k4y8bHWEpc0yBDAn', 'http://www.dianping.com/shop/l6TNZcAdZCZksWy9', 'http://www.dianping.com/shop/k8kSQB7oEmqRIJ8Z', 'http://www.dianping.com/shop/H4GNPARaL1Aam7ZZ', 'http://www.dianping.com/shop/G1F7B8Vp5lbrABs6', 'http://www.dianping.com/shop/H6IIyyJr2dCz2v7V', 'http://www.dianping.com/shop/G4imW3Wb3GZr3uyz','http://www.dianping.com/shop/l1nJ9CiukoTOx3Ky', 'http://www.dianping.com/shop/k8ozO7sH5HOyrDBj', 'http://www.dianping.com/shop/G7DLhPi8avxdMrMH', 'http://www.dianping.com/shop/l80nA1nrwoRprtJV', 'http://www.dianping.com/shop/k9U3PzMqOjbOlm0z', 'http://www.dianping.com/shop/l3LCQY2TQT57WFip', 'http://www.dianping.com/shop/laZhqnH5LjXJBBHK', 'http://www.dianping.com/shop/jWaD3Gi1EAUuW4bq', 'http://www.dianping.com/shop/ivygrBQh9JGnv6M8', 'http://www.dianping.com/shop/G79UB4qUTw3TBJr6', 'http://www.dianping.com/shop/l8Lj6jhH5z3uqo7O', 'http://www.dianping.com/shop/H9OVSU9QVL1Wj2SI', 'http://www.dianping.com/shop/k1Uh9mwaZMLTiMQu','http://www.dianping.com/shop/k7cFALkZpzk8PEcl', 'http://www.dianping.com/shop/l6A9QOErDlVkVSFl', 'http://www.dianping.com/shop/H4ztzpd9qagx6krd', 'http://www.dianping.com/shop/H8EGTUcZZFamIsq3', 'http://www.dianping.com/shop/l6I1aD7tQheoRd7L', 'http://www.dianping.com/shop/G795bGES3qhk0efQ', 'http://www.dianping.com/shop/k5WAMsi9RHGEbtqS', 'http://www.dianping.com/shop/G53tialcZ8iz7BIP', 'http://www.dianping.com/shop/H5YB4CxhYSItO69t', 'http://www.dianping.com/shop/H29MLvVv7tsVxBvH', 'http://www.dianping.com/shop/l4K9hvXJntLdMANR', 'http://www.dianping.com/shop/H8d82PMNsLYtzeG8', 'http://www.dianping.com/shop/l5EfEMZZ6jAg79NC', 'http://www.dianping.com/shop/H6CHCvSomDzWshUY','http://www.dianping.com/shop/l4Dptg3HdQDJMmgn', 'http://www.dianping.com/shop/l1QQdw1CcJwrQSqm', 'http://www.dianping.com/shop/G8kxnB2WAqh1ChIM', 'http://www.dianping.com/shop/H4r4hkdF2eYVeH1Z', 'http://www.dianping.com/shop/EwWhVuoJPRJFkRD3', 'http://www.dianping.com/shop/H5PmjNRQ9OBd3IZJ', 'http://www.dianping.com/shop/H3C6lWb1KeSvtMiO', 'http://www.dianping.com/shop/jLxw9GENusBNYoia', 'http://www.dianping.com/shop/l4ZiynqBiUKjW85a', 'http://www.dianping.com/shop/Hapt1o0EeSpCVsub','http://www.dianping.com/shop/H4cbjgE5jbDPQf7W', 'http://www.dianping.com/shop/G6ZA1VGKiENyDAvX', 'http://www.dianping.com/shop/l48GcbhnMALDgGMx', 'http://www.dianping.com/shop/H6eGgOJB3raMg8uQ', 'http://www.dianping.com/shop/k5Z4TPn2Z6tzoFg6', 'http://www.dianping.com/shop/k3UMEe11gDF3TjXU', 'http://www.dianping.com/shop/gfuJUgb9SsQ6ldS7', 'http://www.dianping.com/shop/G6awACcxnQzrNKvo', 'http://www.dianping.com/shop/H9zMHc9LXzeVbaIf', 'http://www.dianping.com/shop/ElzNReEA7VxNC2ow'
,'http://www.dianping.com/shop/Z1HywNj5izxaC32P', 'http://www.dianping.com/shop/k3WhTnxuCafpCJct', 'http://www.dianping.com/shop/H290nSu9lL4sY1DI', 'http://www.dianping.com/shop/FeVNJ6qXO4rbCkmD', 'http://www.dianping.com/shop/k2e6wxGBZCoRznji', 'http://www.dianping.com/shop/H8F26jegAoolohqR', 'http://www.dianping.com/shop/G4gbqlSdPiKapZ3k', 'http://www.dianping.com/shop/GaxJnQbxtfnKD8q5', 'http://www.dianping.com/shop/k6Lib4mgvgypuPx0', 'http://www.dianping.com/shop/l1XZqfPyRPSbiLpT', 'http://www.dianping.com/shop/k2OrBJeupAlOq9SH', 'http://www.dianping.com/shop/l3GIYBv3kvb2zepF','http://www.dianping.com/shop/GadywHMewVAE3YTB', 'http://www.dianping.com/shop/k7WUKhTArpt2R0uz', 'http://www.dianping.com/shop/l80TTQlO7awMDJwo', 'http://www.dianping.com/shop/k75ET0Bnt0ZrJxiJ', 'http://www.dianping.com/shop/G5XVOvxIxU1DqMcu', 'http://www.dianping.com/shop/k3izZh638pQm4fOc', 'http://www.dianping.com/shop/k497tExHFnJEArmV', 'http://www.dianping.com/shop/G8qXuq0dM5uXBqcg','http://www.dianping.com/shop/k3x4hsjP8X7q0ail', 'http://www.dianping.com/shop/H10CzpdAExBzEDc4', 'http://www.dianping.com/shop/l4lOHDGfa0tnWaMw', 'http://www.dianping.com/shop/G2LzNs2qypEhxSiW', 'http://www.dianping.com/shop/H5zWsTRK4L6hKSo9', 'http://www.dianping.com/shop/EhslRspoKTJIfd48', 'http://www.dianping.com/shop/izzSVFUqmYbTNIDr', 'http://www.dianping.com/shop/k1jHFPO6bIRhwQZY', 'http://www.dianping.com/shop/iQ7i6ScncN1f9iTn','http://www.dianping.com/shop/l3c2EAD55SAU9qAx', 'http://www.dianping.com/shop/k1OVV1EMoxZnE1Ls', 'http://www.dianping.com/shop/l2Fmx147P1466DY6', 'http://www.dianping.com/shop/G1DnkVOyOmMU5Dbb', 'http://www.dianping.com/shop/GaYueDlDbjtaRoVR', 'http://www.dianping.com/shop/H5I5k4sIyLsVBkIT', 'http://www.dianping.com/shop/G1SO4iWmokt8hv10', 'http://www.dianping.com/shop/k7kBvdwUiwEy9PHI', 'http://www.dianping.com/shop/H6t84mlTaRIjndeh', 'http://www.dianping.com/shop/G5rkKhOaTy2kdkN6', 'http://www.dianping.com/shop/H4jmb20huAJCxPIi', 'http://www.dianping.com/shop/l7J2NmtYG6VKilKD'
,'http://www.dianping.com/shop/G1D8TK1Bxf7yDA3p', 'http://www.dianping.com/shop/kaAEYS0nKUC3ZgD1', 'http://www.dianping.com/shop/G9xbEr3rkTH1nUmP', 'http://www.dianping.com/shop/G30SHuqUaKOqXHSD', 'http://www.dianping.com/shop/H8xWTIXsmaaLfW2t', 'http://www.dianping.com/shop/G2VmDBJkwEJe9i9S', 'http://www.dianping.com/shop/kaL9E3mWoqfEVh2N', 'http://www.dianping.com/shop/l494P5R7HafQGmUY', 'http://www.dianping.com/shop/l3EaDfruqXoEc1aD', 'http://www.dianping.com/shop/k1bnnNjjYSyHC8DS', 'http://www.dianping.com/shop/EH8BbJKPhpHcdu9n', 'http://www.dianping.com/shop/l398U7vIx5UEOMiB','http://www.dianping.com/shop/H6Ia6WECd0xDzrsA', 'http://www.dianping.com/shop/H9RrjaomidiYipLh', 'http://www.dianping.com/shop/l9gnPrz411CSikXu', 'http://www.dianping.com/shop/k4wLmIeg4bRm2CmH', 'http://www.dianping.com/shop/G8pDn1m1d4mCTeB9', 'http://www.dianping.com/shop/G1UR69CqyitoiyW7', 'http://www.dianping.com/shop/l8ehPAwe2mLkwjvv', 'http://www.dianping.com/shop/GaSOLVVww7g0K3lU', 'http://www.dianping.com/shop/GamImp96AmQNpbW9', 'http://www.dianping.com/shop/laV1Xrvo4XAZggQg','http://www.dianping.com/shop/l2B1dtV60Iuwwo1i', 'http://www.dianping.com/shop/H6aYXp8ckTlzE1lD', 'http://www.dianping.com/shop/l1OtWxcqT8Zzxe6Z', 'http://www.dianping.com/shop/GavitQYEUCsC4jw7', 'http://www.dianping.com/shop/l5wQjtMX0fG1nEHb', 'http://www.dianping.com/shop/l911kEni57BA4v1J', 'http://www.dianping.com/shop/l6CuBCmoR7dqrfkR', 'http://www.dianping.com/shop/G4FVOBg2AjYAP6XH','http://www.dianping.com/shop/l8hqxj1Evc1qkz5z', 'http://www.dianping.com/shop/Hav8AJWHIlRjCdWO', 'http://www.dianping.com/shop/jaY41LXIJUlj3rme', 'http://www.dianping.com/shop/l7vHlNHoxARO8tXQ', 'http://www.dianping.com/shop/GaSlD6tzPn3TYVXH', 'http://www.dianping.com/shop/k8TObsuwzywyDUCv', 'http://www.dianping.com/shop/G1rKlo8xd5weVT7E', 'http://www.dianping.com/shop/iXMnB6aB5vnfVs6w', 'http://www.dianping.com/shop/l3iFaP6DyMSCm8pn','http://www.dianping.com/shop/l1Kp7YAgPPDoSbZZ', 'http://www.dianping.com/shop/k4pp2tSUHl1KMcRv', 'http://www.dianping.com/shop/H5nmJ7pM8Y7pkF53', 'http://www.dianping.com/shop/G9xEj7Cx2NmrY8AP', 'http://www.dianping.com/shop/G815g0cqfdGUWkeJ', 'http://www.dianping.com/shop/F6otlZPpzrcCgWG3', 'http://www.dianping.com/shop/H3ppfV5EK9uij9Ue', 'http://www.dianping.com/shop/G5EpRHacyGHE2A7I', 'http://www.dianping.com/shop/G8i8IiFqbPmL1e9x', 'http://www.dianping.com/shop/k3rAC1h32z9a1jcA','http://www.dianping.com/shop/H1WT7cWspHo6V5Wp', 'http://www.dianping.com/shop/H3WP78k34rox9eA5', 'http://www.dianping.com/shop/l6l22XIJpUbPvMgL', 'http://www.dianping.com/shop/GadjJcZG9eVtaDIt', 'http://www.dianping.com/shop/H6YAuB8JoQfMIKVZ', 'http://www.dianping.com/shop/k7dov0eaEopKDXxo', 'http://www.dianping.com/shop/G5JM0CTHHPmOw1UZ', 'http://www.dianping.com/shop/k1GwJYeHQsZ2HHtf', 'http://www.dianping.com/shop/l7cUlGvWNKPYDos4'
,'http://www.dianping.com/shop/G9HRPzkd6Jese2ql', 'http://www.dianping.com/shop/k3NL9vtYC1nWZSFi', 'http://www.dianping.com/shop/kaR2aNrgppZrTWY3', 'http://www.dianping.com/shop/H2AUsaIanmygZYq8', 'http://www.dianping.com/shop/G7FKy4ipiVL0DlP0', 'http://www.dianping.com/shop/G36i9qtjMCo88lwB', 'http://www.dianping.com/shop/k9DNIid5cZitMnJl', 'http://www.dianping.com/shop/G9zeguc2GJyRKzM2', 'http://www.dianping.com/shop/k7XT3cPbSy5vmTER', 'http://www.dianping.com/shop/k3vQGWxJdfBtrqB7', 'http://www.dianping.com/shop/l2Mgqr2qTlvIisw9', 'http://www.dianping.com/shop/G8X0ePfN5ANh1nK2','http://www.dianping.com/shop/H1QxPKVPGbseLNBK', 'http://www.dianping.com/shop/k3ZtIugD4UxcWubd', 'http://www.dianping.com/shop/l2qk28DHqQtpWysP', 'http://www.dianping.com/shop/H7TPm0KStfcBucNW', 'http://www.dianping.com/shop/lasrohZLPNnEsZNs', 'http://www.dianping.com/shop/kat6YSrirTtjYF3T', 'http://www.dianping.com/shop/l6Zxkn8bVHxwKpxJ', 'http://www.dianping.com/shop/F4WvBy3gyKbwxSuh', 'http://www.dianping.com/shop/H1vAoQlWppTe1Fd7', 'http://www.dianping.com/shop/H1TiyEXBd4tLR398', 'http://www.dianping.com/shop/H3IR3iMv8MIhp1w5','http://www.dianping.com/shop/EqXZy719JpMjhx2L', 'http://www.dianping.com/shop/H99T8dCGc8lunFtr', 'http://www.dianping.com/shop/H6UHTaL3pq7x8kRs', 'http://www.dianping.com/shop/k7PoqZHURdK9g7ux', 'http://www.dianping.com/shop/l1mDJn61vQhuiQkr', 'http://www.dianping.com/shop/G3f7x7KBgKXJ4llo', 'http://www.dianping.com/shop/la5tqwaxdLlVJSNn', 'http://www.dianping.com/shop/jBXGox0EuNDmK2jV', 'http://www.dianping.com/shop/H3Dj7ggvDC4fe55L', 'http://www.dianping.com/shop/G6h1KbrIpdk1Qord'
,'http://www.dianping.com/shop/jzjAP9N6pT0yzXNw', 'http://www.dianping.com/shop/k1aYwdKMotxs9AGv', 'http://www.dianping.com/shop/l1PrQ21gocuB4jjJ', 'http://www.dianping.com/shop/k6GjIc7P8tDkWEE8', 'http://www.dianping.com/shop/FLCPOh6xDRRMiuA8', 'http://www.dianping.com/shop/l8KlRJ16CT8hVdJR', 'http://www.dianping.com/shop/l9NeMvYAwSMbf6dm', 'http://www.dianping.com/shop/GahTlxVPUNL9guXT', 'http://www.dianping.com/shop/l4v7RDMspaZOcfgw','http://www.dianping.com/shop/Ex7gdrQjk5HeY3mu', 'http://www.dianping.com/shop/l7FG61rL9LwQ8XcX', 'http://www.dianping.com/shop/l3qG1VK2qSoEefVl', 'http://www.dianping.com/shop/G766G9CEPnretnlU', 'http://www.dianping.com/shop/k6zqVCrJfb9Pcydj', 'http://www.dianping.com/shop/G9vkX7Q7SGxnflkA', 'http://www.dianping.com/shop/Fx1T0CTHmPnhrDsN', 'http://www.dianping.com/shop/k6i18lOCp10FOoKU', 'http://www.dianping.com/shop/G7NInHoz02R4tpHk', 'http://www.dianping.com/shop/k6C20lKcyihXcI5r', 'http://www.dianping.com/shop/iuZNtMYvTZkvZ3At'
]
news_urls=[]
for i in urls:
    news_urls.append(i)
print(len(urls))
print(len(news_urls))
print(len(news_urls))
print(len(news_urls))

def pyautogui_action(action):
    if action["name"] in ["move_to_click"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
    elif action["name"] in ["select_all_and_write"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        time.sleep(1)
        pyautogui.hotkey("ctrl", "a")
        write_content = action.get("content","")
        pyautogui.typewrite(write_content)
        pyautogui.press('enter')
    elif action["name"] in ["select_all_and_js_latest"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("ctrl", "a")
        pyautogui.press('backspace')
        pyautogui.press('up')
        pyautogui.press('enter')
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
    elif action["name"] in ["select_item_and_close_tab"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("ctrl", "w")
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
    elif action["name"] in ["url_paste"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        write_content = action.get("content","")
        pyperclip.copy(write_content)
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("ctrl", "l")
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press('enter')
    print(action.get("action_name"))
    action_sleep = action.get("sleep",0)
    time.sleep(action_sleep)

for u in urls:
    print(u)
    page={
        "x":435,
        "y":69,
        "sleep":8,
        "name":"url_paste",
        "content":u,
        "action_name":"访问链接",
    }
    pyautogui_action(page)
    action_item_click_list = [
        {
            "x": 1207,
            "y": 176,
            "sleep": 0.5,
            "name": "move_to_click",
            "content": "",
            "action_name": "清空console",
        },
        {
            "x": 1376,
            "y": 997,
            "sleep": 0.5,
            "name": "select_all_and_copy_and_paste",
            "content":
                '''
result=[]
function Convert_GCJ02_To_BD09($lat,$lng){
    $x_pi = 3.14159265358979324 * 3000.0 / 180.0;
    $x = $lng;
    $y = $lat;
    $z =Math.sqrt($x * $x + $y * $y) + 0.00002 * Math.sin($y * $x_pi);
    $theta = Math.atan2($y, $x) + 0.000003 * Math.cos($x * $x_pi);
    $lng = $z * Math.cos($theta) + 0.0065;
    $lat = $z * Math.sin($theta) + 0.006;
    return [$lng,$lat];
}
result.push(document.getElementsByClassName("shop-name")[0].innerText)
result.push(document.getElementsByClassName("brief-info")[0].getElementsByTagName("span")[0].getAttribute("class").split("mid-str")[1])
result.push(document.getElementsByClassName("brief-info")[0].getElementsByTagName("span")[1].innerText)
try{
result.push(document.getElementsByClassName("brief-info")[0].getElementsByTagName("span")[2].innerText)
}catch{
result.push("null")
}
try{
result.push(document.getElementsByClassName("tel")[0].innerText)
}catch{
document.getElementsByClassName("phone")[0].getElementsByTagName("a")[0].click()
result.push(document.getElementsByClassName("phone")[0].innerText)
}
result.push(document.getElementsByClassName("address")[0].innerText)
result.push(Convert_GCJ02_To_BD09(document.getElementById("map").getElementsByTagName("img")[0].src.split(".png|")[1]))
result_info = {
"shop-name":result[0],
"star":result[1]*0.1,
"comment":result[2],
"consume":result[3],
"tel":result[4],
"address":result[5],
"coordinate":result[6]
}
                ''',
            "action_name": "get店铺信息",
        },
        {
            "x": 1376,
            "y": 997,
            "sleep": 0.5,
            "name": "select_all_and_copy_and_paste",
            "content":
                """
dom=document.createElement("div")
dom.id="wlb_cover"
dom.style.position="fixed"
dom.style.top="0px"
dom.style.right="0px"
dom.style.zIndex=9999999999999999999
                """,
            "action_name": "写入文本框textarea",
        },
        {
            "x": 1376,
            "y": 997,
            "sleep": 0.5,
            "name": "select_all_and_copy_and_paste",
            "content": rf'dom.innerHTML="<textarea id=\"wlb_cover_textarea\">"+JSON.stringify(result_info)+"</textarea>"',
            "action_name": "文本框展示",
        },
        {
            "x": 1376,
            "y": 997,
            "sleep": 0.5,
            "name": "select_all_and_copy_and_paste",
            "content": 'document.body.append(dom)',
            "action_name": "文本框展示",
        },
        {
            "x": 1026,
            "y": 149,
            "sleep": 0.5,
            "name": "select_all_and_copy",
            "content": "",
            "action_name": "copy"
        },
        {
            "x": 431,
            "y": 20,
            "sleep": 1,
            "name": "move_to_click",
            "content": "",
            "action_name": "点击选项卡_pages",
        },
        {
            "x": 533,
            "y": 209,
            "sleep": 1,
            "name": "select_all_and_paste",
            "content": "",
            "action_name": "提交",
        },
        {
            "x": 416,
            "y": 283,
            "sleep": 1,
            "name": "move_to_click",
            "content": "",
            "action_name": "submit",
        },
        {
            "x": 137,
            "y": 24,
            "sleep": 1,
            "name": "move_to_click",
            "content": "",
            "action_name": "切换pgy页面",
        },

    ]

    for action_item_click in action_item_click_list:
        pyautogui_action(action_item_click)



'''

result=[]
result.push(document.getElementsByClassName("shop-name")[0].innerText.split("\n")[0])
result.push(document.getElementsByClassName("brief-info")[0].getElementsByTagName("span")[0].getAttribute("class").split("mid-str")[1])
result.push(document.getElementsByClassName("brief-info")[0].getElementsByTagName("span")[1].innerText)
result.push(document.getElementsByClassName("brief-info")[0].getElementsByTagName("span")[2].innerText)
result.push(document.getElementsByClassName("tel")[0].innerText)
result.push(document.getElementsByClassName("address")[0].innerText)

result_info = {
    "shop-name":result[0],
    "star":result[1]*0.1,
    "comment":result[2],
    "consume":result[3],
    "tel":result[4],
    "address":result[5]
}

dom=document.createElement("div")
dom.id="wlb_cover"
dom.style.position="fixed"
dom.style.top="0px"
dom.style.right="0px"
dom.style.zIndex=9999999999999999999
dom.innerHTML="<textarea id=\"wlb_cover_textarea\">"+JSON.stringify(result_info)+"</textarea>"

document.body.append(dom)


shop-name = document.getElementsByClassName("shop-name")[0].innerText.split("\n")[0]
star = document.getElementsByClassName("brief-info")[0].getElementsByTagName("span")[0].getAttribute("class").split("mid-str")[1]
comment = document.getElementsByClassName("brief-info")[0].getElementsByTagName("span")[1].innerText
consume = document.getElementsByClassName("brief-info")[0].getElementsByTagName("span")[2].innerText
tel = document.getElementsByClassName("tel")[0].innerText
address = document.getElementsByClassName("address")[0].innerText


'''
