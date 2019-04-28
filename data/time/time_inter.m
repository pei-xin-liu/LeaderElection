f=fittype('a*log2(x) + c','independent','x','coefficients',{'a','c'});
[p,S] = fit(x,y,f);
x_plus = linspace(0,105);
coe = coeffvalues(p);
cof = confint(p);
line = 'coe(1)*log2(x_plus)+coe(2)'
up = 
[y_fit,delta] = feval(a);
plot(x,y,'.b','markerSize',15)
hold on
plot(x_plus,y_fit,'r-')
plot(x_plus,y_fit+2*delta,'m--',x_plus,y_fit-2*delta,'m--')
legend({'message vs. n',['message = ', num2str(p(1)), ' * n + ', num2str(p(2))], '95% Prediction Interval'},'Location','best')
set(gca,'FontSize',16);
xlim([0 105]);
grid on;
xlabel('n') 
ylabel('message') 