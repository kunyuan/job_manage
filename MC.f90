PROGRAM MAIN
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
  double precision :: W_N
  double precision :: w1,w2
  integer :: MCOrder
  integer :: Seed
  integer :: ISub
  integer :: InpMC
  character(len=100) :: title

  open(100,file="in00")
  read(100,*) PID
  read(100,*) Typ
  if(Type==2) then
    read(100,*) Ntoss
    read(100,*) Nsamp
    read(100,*) Nstep
    read(100,*) Seed
    read(100,*) IsForever
    read(100,*) IsLoad
    !read(100,*) title
    read(100,*) W_N
    read(100,*) L(1)
    read(100,*) L(2)
    read(100,*) Jcp
    read(100,*) Beta
    read(100,*) MCOrder
    read(100,*) w1,w2
    close(100)
    print *,title
    print *,"weight",w1,w2
  elseif(Type==0) then

END PROGRAM MAIN

