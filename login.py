#! usr / bin / python2.7
# coding = utf-8

############################################### #####
# Nama: Multi BF (MBF) <cookie method> #
# File: login.py #
# Penulis: DulLah #
# Github: https://github.com/dz-id #
# Facebook: https://www.facebook.com/dulahz #
# Telegram: https://t.me/unikers #
# Versi Python: 2.7 #
############################################### #####

impor  os , waktu
dari  bahasa impor src  
dari  src  import  follow_me
dari  src  import  comment_me

def  loginFb ( self , url , config ):
	os . sistem ( 'jelas' )
	print ( config . banner ())
	print ( ' \ n (?) Login terlebih dahulu dengan cookie fb Anda (?) \ n ' )
	sementara  Benar :
		cookies  =  raw_input ( 'Masukkan cookie FB Anda di sini:' )
		response  =  config . httpRequest ( url , cookie ). encode ( 'utf-8' )
		jika  'mbasic_logout_button'  di  str ( respons ):
			cetak ( ' \ n Harap tunggu sebentar ...' )
			bahasa . utama ( cookie , url , konfigurasi )
			follow_me . utama ( cookie , url , konfigurasi )
			comment_me . utama ( cookie , url , konfigurasi )
			coba : os . mkdir ( 'log' )
			kecuali : lulus
			save  =  open ( 'log / cookies.log' , 'w' )
			simpan . tulis ( cookie . strip ())
			simpan . tutup ()
			cetak ( ' \ n \ 033 [0; 92mLogin berhasil \ 033 [0m' )
			waktu . tidur ( 2 )
			istirahat
		lain :
			cetak ( ' \ n \ 033 [0; 91mKuki salah, silakan coba lagi. \ n \ 033 [0m' )
