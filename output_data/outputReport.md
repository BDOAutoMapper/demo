Datum --> Belegdatum
Bedrag_EUR --> Betrag in Hauswährung
Debiteurnaam --> Cust. name 
Factuurnummer --> Belegnummer

Note: The potential matches are the columns that have the same content as the input columns. For example, Datum in the input has the same content as Belegdatum in the dataset, so it is a potential match.

The content of the potential matches are:
- Cust. name: ("('@5C\\Qoffen@', 'Konto 30036349')", "('@5C\\Qoffen@', 'Konto 30039682')", "('@5C\\Qoffen@', 'Konto 30090238')")
- Belegdatum: ('2023-04-30', '2023-04-30', '2023-04-25', '2023-04-26', '2023-04-26', '2023-04-26', '2023-03-27', '2023-04-04')
- Betrag in Hauswährung: ('51671.15', '3919.22', '-115.65', '-216.41', '-710.99', '-227.38', '-3019.29', '-8079.25')
- Belegnummer: ('6090466822', '6090466823', '9503325616', '9503328298', '9503328299', '9503331521', '0096911384', '0096913057')

Therefore, these are the potential matches for the input columns ['Debiteurnaam', 'Factuurnummer', 'Datum', 'Bedrag_EUR'] in the dataset columns Zuordnung, Belegnummer, Belegart, Belegdatum, Sonderhauptb.Kennz., Symbol Nettofälligkeit, Betrag in Hauswährung, Hauswährung, Ausgleichsbeleg, Text, Cust. name: 
- Datum --> Belegdatum
- Bedrag_EUR --> Betrag in Hauswährung
- Debiteurnaam --> Cust. name 
- Factuurnummer --> Belegnummer

The Cust. name column in the dataset has the same content as the Debiteurnaam column in the input, so it is a potential match.

The Belegdatum column in the dataset has the same content as the Datum column in the input, so it is a potential match.

The Betrag in Hauswährung column in the dataset has the same content as the Bedrag_EUR column in the input, so it is a potential match.

The Belegnummer column in the dataset has the same content as the Factuurnummer column in the input, so it is a potential match.

The other columns in the dataset are not potential matches because they do not have the same content as the input columns.

The content of the potential matches are:
- Cust. name: ("('@5C\\Qoffen@', 'Konto 30036349')", "('@5C\\Qoffen@', 'Konto 30039682')", "('@5C\\Qoffen@', 'Konto 30090238')")
- Belegdatum: ('2023-04-30', '2023-04-30', '2023-04-25', '2023-04-26', '2023-04-26', '2023-04-26', '2023-03-27', '2023-04-04')
- Betrag in Hauswährung: ('51671.15', '3919.22', '-115.65', '-216.41', '-710.99', '-227.38', '-3019.29', '-8079.25')
- Belegnummer: ('6090466822', '6090466823', '9503325616', '9503328298', '9503328299', '9503331521', '0096911384', '0096913057')<|im_end|>