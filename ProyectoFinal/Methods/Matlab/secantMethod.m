%Secant Method
%Devolped by: Santiago Alzate, Sebastian Urrego, Esteban Sierra y Alejandro Castaño 
%Updated Last: 04/10/2021

%Inputs: 
%func = continous function  
%x0 = lower bound estimate
%x1 = upper bound estimate
%tol = tolerance
%sc = subinterval count 

%Output 
%x, solution 
%icount = iteration counter 
%err, error 

function [ret] = secantMethod(func,x0,x1,tol,sc)
fx0 = func(x0);
if fx0 == 0
    disp('Solution: %t',x0)
else
    icount = 1;
    err = 1000;
    fx1 = func(x1);
    delta = (fx1-fx0);
    err = Tol+1; 
    ret = [icount,x1,fx1,err] 
    while err > tol && icount <sc && delta ~= 0
        icount = icount + 1;
        temp = x1-f1*(x1-x0)/(fx1-fx0);
        ftemp = func(temp);
        err = abs(temp-x1);
        x0=x1;
        fx0=fx1;
        x1=temp;
        fx1 = ftemp;
        delta = (fx1-fx0)
        ret(cont,1)=icount; 
        ret(cont,2)=x1; 
        ret(cont,3)=fx1; 
        ret(cont,4)=err;
    end
end 
disp(ret)