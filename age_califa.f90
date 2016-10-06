program pop_age_CALIFA
implicit none
integer,parameter::n=5467,nmax=3100000
real,dimension(3,nmax)::C,D
real::x
integer::i,j,nc1


open(1,file="k0127.txt")
open(2,file="idades_k0127.txt")

!read(1,*) C


nc1=0

	do i=1,nmax
 	 read(1,*,end=1) C(1,i), C(2,i),C(3,i)
  	 nc1=nc1+1
     	enddo

	1 continue



j=0

do i=1,nc1
    if (C(3,i).ne.0) then
	j=j+1
	D(1,j)=C(1,i)
	D(2,j)=C(2,i)
	D(3,j)=C(3,i)
	write(2,*) D(1,j), D(2,j), D(3,j)
    endif
enddo




close(1)
close(2)



stop

end program
