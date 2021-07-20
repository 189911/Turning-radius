
      subroutine radio(dim,num_steps,tra,suma)
      integer(kind=4),intent(in):: num_steps,dim
      real(kind=8),dimension(dim,num_steps),intent(in)::tra
      real(kind=8),intent(out):: suma
      integer:: i,s,j
      suma=0.0
      do i=1,num_steps
         do s=1,num_steps
            do j=1,dim
               suma=suma+(tra(j,i)-tra(j,s))**2
            end do
         end do
      end do
      suma=(1/(2*((num_steps)**2.0)))*suma
      end subroutine radio


