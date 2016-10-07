program bina
      implicit none
      INTEGER i,ndatasn,h_err
      INTEGER nc,nc1,npbx, npby,nt,nc2,nc3,nc4
      integer, parameter::nmax=3100000, npmax=2048, nmmax=10000,nm=200000
      parameter(nc=929, npbx= 80,npby=80, nt=6400) !nc # de linhas da imagem
      INTEGER xaux(nc), yaux(nc),xj,yj,j,l,nn,Ni,pp,pix,r80,r20
      real,dimension(4,nmax):: P,Q,R,T
      REAL C3(nc),C4(nc),C5(nc),C6(nc),C7(nc),aux(2),a,b
      INTEGER:: countf(npbx,npby),ntt,np,n,k,iclio,icljo,kmax,iclmax,nct
      real,dimension(3,nt):: S
      LOGICAL pontoencontrado/.FALSE./ !Encontrou um ponto na figura???
      real x(nm),y(nm),z(nm),hists(2,nmmax)
      integer icl(nmmax),itipo(nmmax),hist(nmmax),image(npmax,npmax),ii,jj
      real xx(nm),yy(nm),d,LC
      real cx1,cy1,cx2,cy2,cx3,cy3,cx4,cy4,tetha1,tetha2,tetha3,tetha4
      integer:: ind1,ind2,ind3,ind4

      open(1, file='pop1_k0127.txt',status='old')
      open(2, file='pop2_k0127.txt',status='old')
      open(3, file='pop3_k0127.txt',status='old')
      open(4, file='pop4_k0127.txt',status='old')   
      open(5, file='clump_conc_sym_par.txt', status='old') 
      open(32, file='mapas.txt',status='unknown')
      open(7, file='conc_clump_sym_k0127.txt',status='unknown')
      open(301,file='func_mink_results.txt',status='unknown')
      open(200,file='symmetry_sup.txt',status='unknown')
      open(300,file='symmetry_inf.txt',status='unknown')
      !read(1,*) P


nc1=0
nc2=0
nc3=0
nc4=0


        read(5,*) cx1,cy1,tetha1,cx2,cy2,tetha2,cx3,cy3,tetha3,cx4,cy4,tetha4 


	ind1=1
	ind2=2
	ind3=3
	ind4=4

	do i=1,nmax
 	 read(1,*,end=1) P(1,i), P(2,i),P(3,i),P(4,i)
  	 nc1=nc1+1
     	enddo

	1 continue

	do i=1,nmax
 	 read(2,*,end=2) Q(1,i), Q(2,i),Q(3,i),Q(4,i)
  	 nc2=nc2+1
     	enddo

	2 continue

	do i=1,nmax
 	 read(3,*,end=3) R(1,i), R(2,i),R(3,i),R(4,i)
  	 nc3=nc3+1
     	enddo

	3 continue


	do i=1,nmax
 	 read(4,*,end=4) T(1,i), T(2,i),T(3,i),T(4,i)
  	 nc4=nc4+1
     	enddo

	4 continue
	
	write(7,*) "# Pop	Clumpiness	Concentration	Symmetry	Gini"

!write(*,*) nc1,nc2,nc3,nc4

call clumpiness(ind1,P,nc1,cx1,cy1,tetha1,npbx,npby)
call clumpiness(ind2,Q,nc2,cx2,cy2,tetha2,npbx,npby)
call clumpiness(ind3,R,nc3,cx3,cy3,tetha3,npbx,npby)
call clumpiness(ind4,T,nc4,cx4,cy4,tetha4,npbx,npby)


close(1)
close(2)
close(3)
close(4)
close(5)
close(32)
close(7)
close(200)
close(300)

stop 
end program


!========================================================================
!==============================SUBROTINAS================================
!========================================================================
subroutine clumpiness(ind,P,nc,cx,cy,tetha,npbx,npby)
      INTEGER i,ndatasn,h_err
      INTEGER nc,npbx, npby,nt
      integer, parameter::nmax=3100000, npmax=2048, nmmax=10000,nm=200000
      !parameter(nc=929, npbx= 80,npby=80, nt=6400) !nc # de linhas da imagem
     ! integer,parameter:: nc=nmmax
      INTEGER xaux(nc), yaux(nc),xj,yj,j,l,nn,Ni,pp,pix,r80,r20,k2,ni2
      real,dimension(4,nc):: P
       REAL C3(nc),C4(nc),C5(nc),C6(nc),C7(nc),aux(4),a,b
      INTEGER:: countf(npbx,npby),ntt,np,n,k,iclio,icljo,kmax,iclmax,nct
  !    real,dimension(3,nt):: S
      LOGICAL pontoencontrado/.FALSE./ !Encontrou um ponto na figura???
      real x(nm),y(nm),z(nm),hists(2,nmmax)
      integer icl(nmmax),itipo(nmmax),hist(nmmax),image(npmax,npmax),ii,jj, countf_rodada(npbx,npby)
      real xx(nm),yy(nm),d,LC
      real::Conc1, conc2,conc3,conc4,cx,cy,tetha,bb
      real:: cte, reta, sym1, sym2, SYM
      real:: soma_gini, soma2_gini, cte_G, G, med,soma
      real:: gaux(nc)
nn=0

do 10 yj=npby,1,-1
      do 12 xj=npbx,1,-1
            pontoencontrado=.false.
                  nn=nn+1
    		  itipo(nn)=0
            do 14 i =1,nc
                  if(xj.eq.P(1,i).and.yj.eq.P(2,i))then
                        pontoencontrado=.true.
                  endif
14         enddo
              if(pontoencontrado)then
                  countf(xj,yj)=1
		 ! write(5,*)xj,yj, 1
         	  itipo(nn)=1
              else
                  countf(xj,yj)=0                    
		!  write(5,*)xj,yj, 0
              endif


12    enddo
!write(2,*)
10 enddo

do j=1,npby
   l=npby-j+1
   write(32,'(100i1)') (countf(i,l),i=1,npbx)
enddo

write(32,*)""

!GINI da idade
!
!Subrotina que cálcula o indice de gini segundo a definição dada por Gini(1912)
!G=(1/2*Xmedio*n*(n-1)) * Somatoria(somatoria (abs(Xi-Xj))
!

k2=0

do i=1,nc
	k2=k2+1
	gaux(k2) = P(3,i)
enddo


soma2_gini = 0

 cte_G = 0
G = 0
do i=1,nc
	soma_gini = 0

	do j=0,nc
		ni = abs(gaux(i)-gaux(j))
		soma_gini = soma_gini + ni
	enddo
	
	soma2_gini = soma2_gini + soma_gini

enddo


call avevar(gaux,nc,med,sigma)

 cte_G=(2*med*nc*(nc-1))
 G=(1/cte_G)*soma2_gini



soma=0.


do i=1,nc
	ni2=(2*i-nc-1)*(gaux(i))
	soma=soma+ni2
enddo

!call avevar(gaux,n,med,sigma)

 cte_G2=(med*nc*(nc-1))
 G2=(1/cte_G2)*soma

write(*,*) " "
write(*,*) med, cte_G, soma2_gini, G
write(*,*) med, cte_G2, soma, G2
write(*,*) " "


!=======================
!=======SYMMETRY========

	cte = cy - tetha*cx
	sym1=0
	sym2=0

	do i=1,nc		
		reta = tetha*P(1,i) + cte
		    if (P(2,i).GE.reta) then
			write(200,*) reta, P(1,i), P(2,i), P(3,i)
			sym1=sym1+1
		    else
			write(300,*) reta, P(1,i), P(2,i), P(3,i)
			sym2=sym2+1
		    endif
	enddo


	SYM = 1 - (ABS(sym1 - sym2) / (sym1 + sym2))

	write(*,*) sym1,sym2, SYM


!-------------------------------------
!Rotacao das populações por 180 graus

!do i=1,npbx
!	do j=1,npby
!		countf_rodada(i,j)=countf(npbx-i+1,npby-j)
!	enddo
!enddo
!
!do j=1,npby
!   l=npby-j+1
!   write(52,'(100i1)') (countf_rodada(i,l),i=1,npbx)
!enddo
!write(52,*)""
!------------------------------------



      write(301,*)'FOF/Laerte'

      ntt=npbx*npby
      if(ntt.gt.nm)then
         write(301,*)' FoF: NPIX > NMAX!',ntt,nm
         stop
      endif 

      np=0 
      n=0
      do i=1,npbx
        do j=1,npby
           np=np+1
           if(countf(i,j).eq.1)then
           n=n+1 
           x(n)=i
           y(n)=j
           icl(n)=n
           endif
        enddo
      enddo 
      write(301,*)'no. total de pixels: ',np
      write(301,*) 'no. de pixels acima do limiar: ',n

      do i=1,n
         do j=1,n
            call  distancia(x(i),y(i),x(j),y(j),d)
!     se d=1 os pixels i e j sao conexos
            if(d.eq.1.)then
!     se ambos os pixels ja pertencem a algum objeto, atribuem-se os
!     dois ao objeto de menor numero de identificacao: ii
                  ii=min(icl(i),icl(j))
                  iclio=icl(i)
                  icljo=icl(j)
                  icl(i)=ii
                  icl(j)=ii
!     aos demais pixels dos dois objetos se atribui a mesma identificacao ii
                  do k=1,n
                     if(icl(k).eq.iclio.or.icl(k).eq.icljo)icl(k)=ii
                  enddo
            endif
         enddo
      enddo  

!     determinacao do numero de objetos resultantes
      do k=1,n
         hist(k)=0
      enddo  
      do k=1,n
         l=icl(k)
         hist(l)=hist(l)+1
      enddo  
      nct=0
      kmax=0
      do k=1,n
         if(hist(k).gt.0)then
            nct=nct+1
            write(301,*)nct,hist(k)
            kmax=max(kmax,hist(k))
	    hists(2,nct)=hist(k)
	    hists(1,nct)=nct
            if(hist(k).eq.kmax)iclmax=nct
         endif   
      enddo 
      write(301,*)'n_objetos = ',nct,'  npix do maior objeto: ',kmax
      write(301,*)   '  ident. do maior objeto: ',iclmax

!========================
!======CLUMPINESS========

a=n
b=nct
Lc=a/b



!=======================
!======CONCENTRACAO=====

do i=1,nc
   do k=1,nc
      if (P(4,k).gt.P(4,(k+1))) then
         aux(:) = P(:,k)
         P(:,k)=P(:,(k+1))
         P(:,(k+1))=aux(:)

      end if
   end do
end do

r20=int(0.2*nc)
r80=int(0.8*nc)

Conc1=5*log(P(4,r80)/P(4,r20))

write(7,*) ind,Lc,Conc1,SYM,G2
end



!========================================================================

      subroutine distancia(x,y,xl,yl,d)
!     pixels contiguos com z=zl=1: os 8 com d<=sqrt(2) -> d=1
!     dm2=1.5**2
      parameter(dm2=2.25)
      d=0.
      dist2=(x-xl)**2+(y-yl)**2
      if(dist2.le.dm2)d=1.
      return
      end

!========================================================================

      subroutine percentis(x,n,alfa,xmin,xmax,xinf,xmed,xsup)
!     percentis alfa (0.-50.) de x(n)
!     alfa=25 -> quartis
!     saida: percentil inferior, mediana e percentil superior
      parameter(nmax=100000)
      real x(n),xx(nmax)
      integer indx(nmax)

      if(n.gt.nmax)then
         write(*,*)' n > nmax!!! aumente nmax! '
         stop
      endif   
      if(alfa.ge.50..or.alfa.le.0.)then
         write(*,*)'alfa=',alfa,'     alfa: 0<alfa<50!!! '
         stop
      endif   

      call indexx(n,x,indx)
      xmin=x(indx(1))
      xmax=x(indx(n))
      ip=0
      ip25=0
      ip75=0
      n2=n/2
      ninf=n*alfa/100.
      nsup=n*(100.-alfa)/100.
      if(2*n2.eq.n)ip=1
      if((100.*ninf/alfa).eq.n)ipinf=1
      if((100.*nsup/(100.-alfa)).eq.n)ipsup=1
      if(ip.eq.1)then
         xmed=0.5*(x(indx(n2))+x(indx(n2+1)))        
      else
         xmed=x(indx(n2+1))
      endif   
      if(ipinf.eq.1)then
         xinf=0.5*(x(indx(ninf))+x(indx(ninf+1)))        
      else
         xinf=x(indx(ninf+1))
      endif    
      if(ipsup.eq.1)then
         xsup=0.5*(x(indx(nsup))+x(indx(nsup+1)))        
      else
         xsup=x(indx(nsup+1))
      endif  
      return
      end

!======================================================================== 
      SUBROUTINE indexx(n,arr,indx)
      INTEGER n,indx(n),M,NSTACK
      REAL arr(n)
      PARAMETER (M=7,NSTACK=50)
      INTEGER i,indxt,ir,itemp,j,jstack,k,l,istack(NSTACK)
      REAL a
      do 11 j=1,n
        indx(j)=j
11    continue
      jstack=0
      l=1
      ir=n
1     if(ir-l.lt.M)then
        do 13 j=l+1,ir
          indxt=indx(j)
          a=arr(indxt)
          do 12 i=j-1,1,-1
            if(arr(indx(i)).le.a)goto 2
            indx(i+1)=indx(i)
12        continue
          i=0
2         indx(i+1)=indxt
13      continue
        if(jstack.eq.0)return
        ir=istack(jstack)
        l=istack(jstack-1)
        jstack=jstack-2
      else
        k=(l+ir)/2
        itemp=indx(k)
        indx(k)=indx(l+1)
        indx(l+1)=itemp
        if(arr(indx(l+1)).gt.arr(indx(ir)))then
          itemp=indx(l+1)
          indx(l+1)=indx(ir)
          indx(ir)=itemp
        endif
        if(arr(indx(l)).gt.arr(indx(ir)))then
          itemp=indx(l)
          indx(l)=indx(ir)
          indx(ir)=itemp
        endif
        if(arr(indx(l+1)).gt.arr(indx(l)))then
          itemp=indx(l+1)
          indx(l+1)=indx(l)
          indx(l)=itemp
        endif
        i=l+1
        j=ir
        indxt=indx(l)
        a=arr(indxt)
3       continue
          i=i+1
        if(arr(indx(i)).lt.a)goto 3
4       continue
          j=j-1
        if(arr(indx(j)).gt.a)goto 4
        if(j.lt.i)goto 5
        itemp=indx(i)
        indx(i)=indx(j)
        indx(j)=itemp
        goto 3
5       indx(l)=indx(j)
        indx(j)=indxt
        jstack=jstack+2
        if(jstack.gt.NSTACK)write(*,*) 'NSTACK too small in indexx'
        if(ir-i+1.ge.j-l)then
          istack(jstack)=ir
          istack(jstack-1)=i
          ir=j-1
        else
          istack(jstack)=j-1
          istack(jstack-1)=l
          l=i
        endif
      endif
      goto 1
      END
!  (C) Copr. 1986-92 Numerical Recipes Software YLu.

!==========================================================

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


