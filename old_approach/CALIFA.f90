!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!PROGRAMA PARA CALCULAR AS POPULAÇÕES ESTELARES E PARÂMETROS
!MORFOLÓGICOS E TOPOGRÁFICOS ASSOCIADOS A ELAS.
!
!Criado por Patricia Novais
!Maio de 2015
!
!Versão 1.0
!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

program pop_age_CALIFA
implicit none
integer,parameter:: nmax=3100000, npmax=2048
!real,parameter::rp=29.17237
real,dimension(3,nmax)::C,D
real,dimension(3)::aux
real:: raux(nmax),caux(nmax),taux(nmax)
real::x,re
integer::cx,cy,n
real:: rm,sigm,r_med,t_m,sig_t,t_med,R,sig
integer::i,j,k,nc,m10,m01,nc1


!=============================================================
!raux é o raio calculado para cada píxel, utilizando geometria
!básica, para usar na funcao AVEVAR e MDIAN1.
!taux é idade de cada píxel, calculado pelo CALIFA.
!re é o raio de equivalente do objeto, dado por
!	re = (Nt/pi)^1/2 = (A/pi)^1/2
!onde Nt=A é o número de píxeis do objeto inteiro, i.e, sua 
!area total
!R é o raio da população normalizado por re
!=============================================================

open(5,file="k0127.txt")
open(8,file="idades_k0127.txt")
open(7,file='idades_ord_k0127.txt')
open(1,file='pop1_k0127.txt')
open(2,file='pop2_k0127.txt')
open(3,file='pop3_k0127.txt')
open(4,file='pop4_k0127.txt')
open(6,file="k0127_idades.txt")
!open(15,file="ord_idades.txt")
open(10,file="estatisticas_pop_k0127.txt")
open(11,file='parametros_de_forma_k0127.txt')
open(12,file='minkowski_function.txt')
open(13,file="momentos_k0127.txt")
open(14,file="all_parametros_k0127.txt")
open(15,file="clump_conc_sym_par.txt")

!read(5,*) C



nc1=0

	do i=1,nmax
 	 read(5,*,end=1) C(1,i), C(2,i),C(3,i)
  	 nc1=nc1+1
     	enddo

	1 continue


 n = nc1

write(10,*) "# Pop.	Rm/Re	sigma_r	tm	sigma_t	kurtx 	kurty 	skewx 	skewy"
write(11,*) '#  Pop. Xc	Yc	tetha(rad)  mu_11    mu_20   mu_02   a    b  f = (a-b)/a    excent flong  fcomp'
write(13,*) " # Pop. I1	I2	I3	I4	I5	I6	I7"
write(14,*) "# Pop. I1	I2	I3	I4	I5	I6	I7   mu_11    mu_20   mu_02   a    b  &
                & media(a+b)   R R/Re Sigm_R/Re tetha(rad)  excent flong  fcomp   T sigm_T intensidade"

                


!Separando, a partir do arquivo original, os píxeis que contem
!informações, i.e., idade diferente de zero.
j=0

do i=1,n
    if (C(3,i).ne.0) then
	j=j+1
	D(1,j)=C(1,i)
	D(2,j)=C(2,i)
	D(3,j)=C(3,i)
	write(8,*) D(1,j), D(2,j), D(3,j)
    endif
enddo



! Ordenação dos píxeis pela idade
do i=1,j
   do k=1,j
      if (D(3,k).gt.D(3,(k+1))) then
         aux(:) = D(:,k)
         D(:,k)=D(:,(k+1))
         D(:,(k+1))=aux(:)

      end if
   end do
end do

!Impressão dos píxeis ordenados
do i=1,j
	write(7,*) D(1,i), D(2,i), D(3,i)
enddo


!======================================================
!================CENTROIDES DA IMAGEM==================
!======================================================
!xc = M10/M00
!yc = M01/M00
!
!onde xc e yc são os centróides da imagem, M10, M01 e 
!M00 os momentos não centrais, onde
!
!Mpq=Somatorio(x^p.y^q)
!------------------------------------------------------

m10=0
m01=0


do i=1,j
	m10=m10+D(1,i)
	m01=m01+D(2,i)
enddo


cx=m10/j
cy=m01/j


!write(*,*) cx,cy

!Abaixo, a determinação dos bins de população, com cada
!bin com o mesmo número de pontos, além do cálculo do 
!raio médio e mediano (+sigma) e idade média e mediana
!(+sigma)

!Raio equivalente
re=sqrt(j/3.14)


!======================================================

	call parameters(1,D,j,1,j/4,cx,cy,Re,R,sig,t_m,sig_t)
 
	call parameters(2,D,j,(j/4)+1,(2*j/4),cx,cy,Re,R,sig,t_m,sig_t) 

	call parameters(3,D,j,(2*j/4)+1,(3*j/4),cx,cy,Re,R,sig,t_m,sig_t) 

	call parameters(4,D,j,(3*j/4)+1,j,cx,cy,Re,R,sig,t_m,sig_t) 



write(15,*) "Xc	Yc	Tetha(rad)"
close(1)
close(2)
close(3)
close(4)
close(5)
close(6)
close(7)
close(8)
close(10)
close(11)
close(13)
close(14)
close(15)


stop

end program

!========================================================================
!==============================SUBROTINAS================================
!========================================================================


       SUBROUTINE avevar(data,n,ave,var)
      INTEGER n
      REAL ave,var,data(n)
      INTEGER j
      REAL s,ep
      ave=0.0
      do 11 j=1,n
        ave=ave+data(j)
11    continue
      ave=ave/n
      var=0.0
      ep=0.0
      do 12 j=1,n
        s=data(j)-ave
        ep=ep+s
        var=var+s*s
12    continue
      var=(var-ep**2/n)/(n-1)
      var=sqrt(var)
      return
      END
!  (C) Copr. 1986-92 Numerical Recipes Software YLu.

!========================================================================
      SUBROUTINE MDIAN1(X,N,YMED)
      DIMENSION X(N)
      CALL SORT(N,X)
      N2=N/2
      IF(2*N2.EQ.N)THEN
        YMED=0.5*(X(N2)+X(N2+1))
      ELSE
        YMED=X(N2+1)
      ENDIF
      RETURN
      END

!========================================================================

      SUBROUTINE SORT(N,RA)
      DIMENSION RA(N)
      L=N/2+1
      IR=N
10    CONTINUE
        IF(L.GT.1)THEN
          L=L-1
          RRA=RA(L)
        ELSE
          RRA=RA(IR)
          RA(IR)=RA(1)
          IR=IR-1
          IF(IR.EQ.1)THEN
            RA(1)=RRA
            RETURN
          ENDIF
        ENDIF
        I=L
        J=L+L
20      IF(J.LE.IR)THEN
          IF(J.LT.IR)THEN
            IF(RA(J).LT.RA(J+1))J=J+1
          ENDIF
          IF(RRA.LT.RA(J))THEN
            RA(I)=RA(J)
            I=J
            J=J+J
          ELSE
            J=IR+1
          ENDIF
        GO TO 20
        ENDIF
        RA(I)=RRA
      GO TO 10
      END

!========================================================================
!========================================================================

subroutine parameters(p,T,j,k,m,cx,cy,Re,R,sig,t_m,sig_t) 
implicit none

integer:: cx,cy,rp,i,m,nc,k,j,p,l,s,xj,yj,nobj
integer, parameter::nmax=3100000, npmax=2048
integer, parameter:: n=3417, npbx=105,npby=84
real, dimension(3,n):: T
real:: raux(nmax),taux(nmax),uraux(nmax),graux(nmax),riaux(nmax),rzaux(nmax)
integer::xaux(nmax),yaux(nmax),npixobj(nmax)
real::R,sig,t_m,sig_t, soma_x, soma_y,Re, x_cent, y_cent, rm, sigm, ur_m,sig_ur
real:: gr_m, sig_gr, ri_m, sig_ri, rz_m, sig_rz,soma_n, soma11, soma20, soma02
real:: soma_m11, soma_m20, soma_m02, exc, flong, fcomp,exc2, fcomp2,soma30
real:: soma40,soma04
real:: soma03, I1,I2,I3,I4,I5,I6,I7,mu11,mu20,mu02
real:: n11,n10,n12,n21,n20,n02,n22,n03,n30
real:: soma12 , soma21,tetha3
real:: a,b,tetha, f, d, percent,xxmin,xxmax,xxinf,xxmed,xxsup, t_med, tetha2
integer::countf1(npmax,npmax),countf(npmax,npmax)
LOGICAL pontoencontrado/.FALSE./ !
real:: aa,bb,cc,w,ll,ang
real::dd,ee, intens, kurtx,kurty,skewx,skewy

character(len=30):: Formats

! inicialização dos contadores
do i=1,j
	raux(j) = 0
	taux(j) = 0
        xaux(j) = 0
        yaux(j) = 0
	
enddo

! inicialização dos contadores
rm=0.
nc=0

soma_x=0
soma_y=0
soma_n=0


!=============================================================
!------Impressao das coordenadas, idade e raio/Re-------------
!=============================================================

!write(p,*) "#	 X		 Y		Idade 		raio/Re"


do i=k,m
    nc=nc+1
    xaux(nc)=int(T(1,i))
    yaux(nc)=int(T(2,i))
    raux(nc)=sqrt((T(1,i)-cx)**2+(T(2,i)-cy)**2)
    taux(nc) = T(3,i)

 	write(p,*) T(1,i), T(2,i),T(3,i), raux(nc)/Re
 	
    soma_x=soma_x+T(1,i) 
    soma_y=soma_y+T(2,i)
    soma_n=soma_n+1

enddo


!Centroides
x_cent=soma_x/soma_n
y_cent=soma_y/soma_n


!percent=25.0
!call percentis(taux,nc,percent,xxmin,xxmax,xxinf,xxmed,xxsup)


!medias e sigmas do raio e idade 

 	call avevar(raux,nc,R,sigm)

 	call avevar(taux,nc,t_m,sig_t)

 	
sig = sigm/Re
Formats = "(1I6, 17F10.5)"

!população, raio medio, sigma do raio medio, idade media, sigma 
!da idade media, idade mediana, idade minima, idade inferior
!idade superior, idade máxima


!=============================================================
!CALCULO DOS MOMENTOS (CENTRAIS e NAO CENTRAIS)
!
!Ver:http://pt.wikipedia.org/wiki/Momentos_Invariantes_de_uma_Imagem
!
!=============================================================

!------------
!M_11 nao central

soma_m11 =0

do i=k,m
    soma_m11 = soma_m11 + ((T(1,i))*(T(2,i)))
enddo


!------------
!M_20 nao central

soma_m20 =0

do i=k,m
    soma_m20 = soma_m20 + ((T(1,i))*(T(1,i)))
enddo


!------------
!M_02 nao central

soma_m02 =0

do i=k,m
    soma_m02 = soma_m02 + ((T(2,i))*(T(2,i)))
enddo

!-------------------------------------------------------------
! MOMENTOS CENTRAIS, invariantes por translação
!idem referência acima
!-------------------------------------------------------------
!somaij é o momento central
! mu_ij é o momento central normalizado por M00
! mu_ij = somaij/M00
!



soma11=0

do i=k,m
    soma11 = soma11 + ((T(1,i)-cx)*(T(2,i)-y_cent))
enddo

mu11=soma11/j

!------------
!mu_21


soma21=0

do i=k,m
    soma21 = soma21 + (((T(1,i)-cx)**2)*(T(2,i)-y_cent))
enddo


!------------
!mu_12

soma12=0

do i=k,m
    soma12 = soma12 + ((T(1,i)-cx))*((T(2,i)-y_cent)**2)
enddo

!------------
! mu_20

soma20=0

do i=k,m
    soma20 = soma20 + ((T(1,i)-cx)**2)
enddo

mu20=soma20/j

!------------
! mu_02

soma02=0

do i=k,m
    soma02 = soma02 + ((T(2,i)-y_cent)**2)
enddo

mu02=soma02/j

!------------
!mu_30

soma30=0

do i=k,m
    soma30 = soma30 + ((T(1,i)-cx)**3)
enddo

!------------
!mu_03

soma03=0

do i=k,m
    soma03 = soma03 + ((T(2,i)-y_cent)**3)
enddo

!------------
!mu_40

soma40=0

do i=k,m
    soma40 = soma40 + ((T(1,i)-cx)**4)
enddo

!------------
!mu_04

soma04=0

do i=k,m
    soma04 = soma04 + ((T(2,i)-y_cent)**4)
enddo


!CALCULO DOS MOMENTOS INVARIANTES POR ESCALA
!ordem (p+q) até 3.

n11= soma11/((soma_n)**2)

n12 = soma12/((soma_n)**(2.5))

n21 = soma21/((soma_n)**(2.5))

n02 = soma02/((soma_n)**2)

n20 = soma20/((soma_n)**2)

n30 = soma30/((soma_n)**(2.5))

n03 = soma03/((soma_n)**(2.5))



!CALCULO DOS MOMENTOS INVARIANTES POR TRANSLAÇÃO, ESCALA e ROTACÃO
I1= n02 + n20

I2 = ((n20-n02)**2) + 4*((n11)**2)

I3 = (n30 - 3*n12)**2 + (3*n21 - n03)**2

I4 = (n30 + 3*n12)**2 + (3*n21 + n03)**2

I5 = (n30 - 3*n12)*(n30 + n12)*(((n30 + n12)**2) - 3*((n21 + n03)**2)) +&
& (3*n21 - n03)*(n12 + n03)*(3*((n30 + n12)**2) - ((n21 + n03)**2)) 

I6 = (n20 - n02)*((n30 + n12)**2 - (n21 + n03)**2) + 4*n11*(n30 + n12)*(n21 + n03)

I7 = (3*n21 - n03)*(n30 + n12)*((n30 + n12)**2 - 3*(n21 + n03)**2) - (n30 - 3*n12)*(n21 + n03)*(3*(n30 + n12)**2 - (n21 + n03)**2)



write(13,*) p,I1,I2,I3,I4,I5,I6,I7


!PARAMETROS DA ELIPSE

!calculo dos semi-eixos da elipse segundo o que foi descrito
!em Prokop&Reeves
!http://www.via.cornell.edu/ece547/text/survey.pdf
!
!
dd = (soma20 + soma02)
ee = (soma20 - soma02)*(soma20 - soma02) + 4*(soma11)*(soma11)

a = sqrt((2*(dd + sqrt(ee)))/j)

b = sqrt((2*(dd - sqrt(ee)))/j)


!razão dos semi-eixos
!f = (a+b)/2

f = (a+b)/2


!achatamento
!f = 1 - (b/a)

!ORIENTACAO

tetha  = 0.5*atan((2*soma11)/(soma20 - soma02))
tetha2 = acos(b/a)
tetha3 = 0.5*atan((2*mu11)/(mu20 - mu02))

d=1


!write(55,*) tetha, tetha3, tetha2


!EXCENTRICIDADE
exc = 1 - (b/a)

!FATOR DE ELONGACAO

flong = sqrt((mu02/mu20))

! FATOR DE COMPACTICIDADE

fcomp = (soma_n*soma_n)/(2*3.1415*sqrt( (soma20*soma20 + soma02*soma02) ))


! Intensidade da imagem da elipse, segundo referencia acima
!Prokop&Reeves
!
intens=j/(3.1415*a*b)


!KURTOSE & SKEWNESS
!(curtose e obliquidade)
!segundo a mesma referencia anterior
!

kurtx = (soma40/(soma20*soma20)) - 3
kurty = (soma04/(soma02*soma02)) - 3

skewx = soma30/((soma20)**(3/2))
skewy = soma03/((soma02)**(3/2))

write(10,Formats) p, R/Re,sig,t_m,sig_t,kurtx,kurty,skewx,skewy

write(11,*) p, x_cent, y_cent, tetha,soma11, soma20, soma02, a, b, f,  exc, flong,fcomp

write(14,*) p,I1,I2,I3,I4,I5,I6,I7, soma11, soma20, soma02, a, b, f, R, R/Re, sig, tetha,  &
            & exc, flong,fcomp,t_m,sig_t, intens!,xxmed, xxmin,xxinf,xxsup,xxmax,

write(15,*) x_cent,y_cent,tetha

end

