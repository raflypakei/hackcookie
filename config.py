#! usr / bin / python2.7
# coding = utf-8

############################################### #####
# Nama: Multi BF (MBF) <cookie method> #
# File: config.py #
# Penulis: DulLah #
# Github: https://github.com/dz-id #
# Facebook: https://www.facebook.com/dulahz #
# Telegram: https://t.me/unikers #
# Versi Python: 2.7 #
############################################### #####

 permintaan impor

 Konfigurasi kelas :
	def  loadCookie ( mandiri ):
		coba :
			file  =  open ( 'log / cookies.log' , 'r' )
			cookie  =  file . baca ()
			file . tutup ()
			kembalikan  kue . strip ()
		kecuali  IOError :
			mengembalikan  False

	 spanduk def ( mandiri ):
		kembalikan  '' ' \ n
\ 033 [0; 96m __ ___ ____ _ ___ ____
\ 033 [0; 96m / | / / _ __ / / / _ (_) / _) / __ /   \ 033 [0m || Diciptakan oleh Rafly
\ 033 [0; 96m / / | _ / / // / / __ / / / _ / _ /     \ 033 [0m || Rafly pake i
\ 033 [0; 96m / _ / / _ / \ _, _ / _ / \ __ / _ / / ____ / _ / \ 033 [0; 91mv2.0 \ 033 [0m || Wa 082290232340'' '

	def  httpRequest ( self , url , cookies ):
		coba :
			mengembalikan  permintaan . dapatkan ( url , cookies  = { 'cookie' : cookies }). teks
		kecuali  permintaan . pengecualian . RequestException :
			keluar ( ' \ n \ n \ 033 [0; 91mKoneksi sambungan, periksa koneksi Anda !! \ 033 [0m' )

	def  httpRequestPost ( mandiri , url , cookie , params ):
		coba :
			mengembalikan  permintaan . posting ( url , data  =  params , cookies  = { 'cookie' : cookies }). teks
		kecuali  permintaan . pengecualian . RequestException :
			keluar ( ' \ n \ n \ 033 [0; 91mKoneksi sambungan, periksa koneksi Anda !! \ 033 [0m' )