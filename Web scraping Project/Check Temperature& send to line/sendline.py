from songline import Sendline

token ='FA33KVNMXUBC9Bq2DwYpj0nrMiLS3hew3eDRFOa08C9'

messenger = Sendline(token)

#messenger.sendtext('สวัสดีคับ')
#messenger.sticker('403','1','อะไรคับเนี่ย')

img = 'https://static.thairath.co.th/media/Dtbezn3nNUxytg04acvLL8CnMEukJNNB4mNK4YF2XHZqpp.jpg'
messenger.sendimage(img)
