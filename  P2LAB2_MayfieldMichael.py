current_price = int(input())
last_months_price = int(input())
est_mortgage = current_price * 0.051/12
print ('This house is', f'${current_price}.', 'The change is', f'${current_price - last_months_price}', 'since last month.')
print ('The estimated monthly mortgage is', f'${est_mortgage:.2f}.')

   
