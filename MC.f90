PROGRAM MAIN
	USE IFPORT
  implicit none
  integer :: PID
  integer :: Typ
  integer :: L(2)
  integer :: Ntoss
  integer :: Nsamp
  logical :: IsForever
  logical :: IsLoad
  integer :: NStep
  double precision :: Jcp
  double precision :: beta
  double precision,allocatable :: Reweight(:)
  double precision :: wormnorm
  double precision :: w1,w2
  integer :: MCOrder
  integer :: RNDSeed
  integer :: ISub
  integer :: InpMC
  integer :: i
  character(len=100) :: title
  character(len=100) :: infile
  INTEGER(4) delay

  read(*,'(A)') infile
  write(*,*) infile
  open(100,file=trim(adjustl(infile)))
  write(*,*) "Opened!"
  read(100,*) PID
  read(100,*) L(1)
  read(100,*) L(2)
  read(100,*) Jcp
  read(100,*) Beta
  read(100,*) MCOrder
  read(100,*) IsLoad
  read(100,*) Typ
  allocate(Reweight(MCOrder))
  if(Typ==2) then
    read(100,*) IsForever
    read(100,*) Ntoss
    read(100,*) Nsamp
    read(100,*) Nstep
    read(100,*) RNDSeed
    !read(100,*) title
    read(100,*) wormnorm
    read(100,*) Reweight
  elseif(Typ==1 .or. Typ==3) then
    read(100,*) title
  endif

  close(100)
  print *,MCOrder
  print *,"weight",Reweight

  delay    = 10000

 print *, "Sleep for 10s"
 CALL SLEEPQQ(delay)
 print *, "Sleep for another 10s"
 CALL SLEEPQQ(delay)

END PROGRAM MAIN

