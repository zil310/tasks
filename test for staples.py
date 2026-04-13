import staples
assert staples.is_balance(['{''('')''[''('')'']''}''<''<''<''>''>''>']), "Не робит"
assert staples.is_balance(['a''(''b''[''c''{''d''}''e'']''f'')''g']), "Не робит"
assert staples.is_balance([]), "Не робит"
assert staples.is_balance(['(''(''(']), "Error"
assert staples.is_balance(['[''('']'')']), "Error"