PROGRAM MAIN
  implicit none
  integer :: L(2)
  integer :: Ntoss
  integer :: Nsamp
  integer :: IsForever
  integer :: NStep
  double precision :: Jcp
  double precision :: beta
  integer :: MCOrder
  integer :: Seed
  integer :: ISub
  integer :: InpMC
  integer :: ID
  character(len=100) :: title

  print *, 'L(1), L(2), Ntoss, Nsamp, IsForever, NStep, Jcp, beta, MCOrder, Seed, ISub, InpMC, ID, title'
  read  *,  L(1), L(2), Ntoss, Nsamp, IsForever, NStep, Jcp, beta, MCOrder, Seed, ISub, InpMC, ID, title

END PROGRAM MAIN

