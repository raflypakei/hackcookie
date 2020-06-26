#! usr / bin / python2.7
# coding = utf-8

############################################### #####
# Nama: Multi BF (MBF) <cookie method> #
# File: main.py #
# Penulis: DulLah #
# Github: https://github.com/dz-id #
# Facebook: https://www.facebook.com/dulahz #
# Telegram: https://t.me/unikers #
# Versi Python: 2.7 #
############################################### #####

impor  os , waktu
dari  konfigurasi impor aplikasi  
dari  login impor aplikasi  
dari  celah impor aplikasi  
dari  src  import  friends_list
dari  src  import  friends
dari  src  import  search_name
dari  src  import  suka
dari  bs4  impor  BeautifulSoup  sebagai  parser

class  Brute ( objek ):
	def  __init__ ( mandiri , url ):
		diri . url  =  url
		diri . config  =  config . Konfigurasi ()
		diri . cookie  =  sendiri . config . loadCookie ()
		diri . menu  =  ' \ n '
		diri . menu  + =  '[ \ 033 [0; 96m01 \ 033 [0m] Dump Id Daftar teman \ n '
		diri . menu  + =  '[ \ 033 [0; 96m02 \ 033 [0m] Dump Id Teman \ n '
		diri . menu  + =  '[ \ 033 [0; 96m03 \ 033 [0m] Id Dump dengan Nama pencarian \ n '
		diri . menu  + =  '[ \ 033 [0; 96m04 \ 033 [0m] Id Dump dari status suka \ n '
		diri . menu  + =  '[ \ 033 [0; 96m05 \ 033 [0m] Mulai Retak \ n '
		diri . menu  + =  '[ \ 033 [0; 96m00 \ 033 [0m] Hapus cookie \ n '
		jika  diri . cookie  ==  Salah :
			login . loginFb ( self , self . url , self . config )
			diri . cookie  =  sendiri . config . loadCookie ()

	 mulai def ( diri ):
		respon  =  diri . config . httpRequest ( self . url + '/profile.php' , self . cookie ). encode ( 'utf-8' )
		jika  'mbasic_logout_button'  di  str ( respons ):
			diri . utama ( respons )
		lain :
			os . hapus ( 'log / cookies.log' )
			cetak ( ' \ n \ 033 [0; 91m [PERINGATAN] Cookie tidak valid, silakan login lagi. \ 033 [0m' )
			raw_input ( ' \ n [Tekan Enter]' )
			login . loginFb ( self , self . url , self . config )
			diri . cookie  =  sendiri . config . loadCookie ()
			diri . mulai ()
			keluar ()

	def  main ( self , response ):
		os . sistem ( 'jelas' )
		print ( self . config . banner ())
		html  =  parser ( respons , 'html.parser' )
		cetak ( '_________________________________________________________________' )
		print ( ' \ n ( \ 033 [0; 96m • \ 033 [0m) AKTIF PENGGUNA:' . decode ( 'utf-8' ) + html . title . teks . teks . atas ())
		cetak ( '_________________________________________________________________' )
		mencetak ( diri . menu )
		coba :
			pilih  =  int ( raw_input ( 'Pilih >>' ))
		kecuali  ValueError :
			keluar ( ' \ n \ 033 [0; 91mAnda bodoh. \ 033 [0m' )
		jika  pilih  ==  1 :
			keluar ( friends_list . main ( self , self . cookie , self . url , self . config ))
		Elif  pilih  ==  2 :
			keluar ( teman . utama ( self , self . cookie , self . url , self . config ))
		Elif  pilih  ==  3 :
			keluar ( search_name . main ( self , self . cookie , self . url , self . config ))
		Elif  pilih  ==  4 :
			keluar ( suka . utama ( self , self . cookie , self . url , self . config ))
		Elif  pilih  ==  5 :
			keluar ( crack . Brute (). main ())
		Elif  pilih  ==  0 :
			ask  =  raw_input ( ' \ n Yakin? [y / N]:' )
			jika  ditanya . lebih rendah () ==  'y' :
				print ( ' \ n Menghapus cookie ...' )
				waktu . tidur ( 2 )
				os . hapus ( 'log / cookies.log' )
				cetak ( ' \ n \ 033 [0; 92mSukses dihapus! \ 033 [0m' )
				waktu . tidur ( 2 )
				login . loginFb ( self , self . url , self . config )
				diri . cookie  =  sendiri . config . loadCookie ()
				diri . mulai ()
			lain :
				diri . cookie  =  sendiri . config . loadCookie ()
				cetak ( ' \ n dibatalkan!' )
				diri . mulai ()
		lain : keluar ( ' \ n \ 033 [0; 91mAnda bodoh. \ 033 [0m' )