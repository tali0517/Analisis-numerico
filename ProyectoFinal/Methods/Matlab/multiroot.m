% Multiple Roots 
%Devolped by: Santiago Alzate, Sebastian Urrego, Esteban Sierra y Alejandro Castaño 
%Updated Last: 04/10/2021

%Inputs: 
%func = continous function
%fprime = func's ddx and continous 
%f2prime = func's second derivative, continous 
%x0 = lower bound estimate
%tol = tolerance
%sc = subinterval count 

%Output 
%x, solution 
%icount = iteration counter 
%err, error 

function ret = multiroot(func, fprime, f2prime, x0, tol)
err = 10;
icount = 1
while abs(err) >tol
    temp = x0-func(x0)*fprime(x0)/((fprime(x0))^2-func(x0)*f2prime(x0));
    err = ((temp-x0)/temp*100);
    x0=temp;
    icount = icount +1; 
end 
disp('Root: %f in %i iterations',x0,icount);