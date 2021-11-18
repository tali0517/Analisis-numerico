%Newton Method 
%This program helps to find the solution to equation f(x)=0  through
%Newton's method. 
%Devolped by: Santiago Alzate, Sebastian Urrego, Esteban Sierra y Alejandro Castaño 
%Updated Last: 03/10/2021

%Inputs: 
%func = continous function 
%df = ddx for func, continous as well. 
%startp = starting approximation 
%tol = tolerance 
%sc = subinterval count 

%Output 
%x, solution 
%icount = iteration counter 
%err, error 

function [x, icount, err] = newton(func, df, startp, tol, sc)
x0 = startp;
err=1000;
cont=0;

while E>tol && cont < sc
    x1 = x0 - func(x0)/df(x0);
    err = abs(x1-x0);
    icount = icount+1;
    %Falta retornar valores de la iteracion fact ^ fant. 
    x0 = x1;
end
disp(x0, err, icount)





