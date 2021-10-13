import numpy as np
import streamlit as st
import pandas as pd
import pymongo

client= pymongo.MongoClient("mongodb://localhost:27017/", username='root', password='example')
db = client["fmi"]
col = db["measurements"]

stations = pd.Series(sorted(['Porvoo Kilpilahti satama', 'Jomala Maarianhamina lentoasema', 'Parainen Utö', 'Lemland Nyhamn', 'Jomala Jomalaby', 'Hammarland Märket', 'Kökar Bogskär', 'Parainen Fagerholm', 'Kumlinge kirkonkylä', 'Kaarina Yltöinen', 'Kemiönsaari Vänö', 'Hanko Tulliniemi', 'Turku Rajakari', 'Turku Artukainen', 'Kemiönsaari Kemiö', 'Hanko Tvärminne', 'Salo Kärkkä', 'Raasepori Jussarö', 'Salo Kiikala lentokenttä', 'Vantaa Helsinki-Vantaan lentoasema', 'Inkoo Bågaskär', 'Helsinki Kaisaniemi', 'Lohja Porla', 'Vihti Maasoja', 'Helsinki Harmaja', 'Kirkkonummi Mäkiluoto', 'Helsinki Helsingin majakka', 'Helsinki Kumpula', 'Helsinki Malmi lentokenttä', 'Porvoo Kalbådagrund', 'Porvoo Emäsalo', 'Porvoo Harabacka', 'Kotka Rankki', 'Loviisa Orrengrund', 'Kotka Haapasaari', 'Pori lentoasema', 'Kustavi Isokari', 'Rauma Kylmäpihlaja', 'Pori rautatieasema', 'Turku lentoasema', 'Kokemäki Tulkkila', 'Jokioinen Ilmala', 'Pirkkala Tampere-Pirkkala lentoasema', 'Tampere Härmälä', 'Somero Salkola', 'Hyvinkää Hyvinkäänkylä', 'Nurmijärvi Röykkä', 'Hämeenlinna Katinen', 'Hattula Lepaa', 'Hämeenlinna Lammi Pappila', 'Asikkala Pulkkilanharju', 'Kouvola Utti lentoasema', 'Kouvola Anjala', 'Heinola Asemantaus', 'Kouvola Utti Lentoportintie', 'Virolahti Koivuniemi', 'Lappeenranta lentoasema', 'Lappeenranta Konnunsuo', 'Lappeenranta Lepola', 'Lappeenranta Hiekkapakka', 'Parikkala Koitsanlahti', 'Kaskinen Sälgrund', 'Pori Tahkoluoto satama', 'Kristiinankaupunki Majakka', 'Karvia Alkkia', 'Kauhajoki Kuja-Kokko', 'Kankaanpää Niinisalo lentokenttä', 'Virrat Äijänneva', 'Tampere Siilinkari', 'Jämsä Halli lentoasema', 'Juupajoki Hyytiälä', 'Jämsä Halli Lentoasemantie', 'Jyväskylä lentoasema', 'Luhanka Judinsalo', 'Joutsa Savenaho', 'Mikkeli lentoasema', 'Juva Partala', 'Varkaus Kosulanniemi', 'Savonlinna lentoasema', 'Rantasalmi Rukkasluoto', 'Savonlinna Punkaharju Laukansaari', 'Tohmajärvi Kemie', 'Vaasa lentoasema', 'Mustasaari Valassaaret', 'Korsnäs Bredskäret', 'Maalahti Strömmingsbådan', 'Vaasa Klemettilä', 'Seinäjoki Pelmaa', 'Kauhava lentokenttä', 'Ähtäri Inha', 'Halsua Purola', 'Alajärvi Möksy', 'Multia Karhila', 'Viitasaari Haapaniemi', 'Vesanto kirkonkylä', 'Siilinjärvi Kuopio lentoasema', 'Kuopio Maaninka', 'Kuopio Ritoniemi', 'Kuopio Savilahti', 'Rautavaara Ylä-Luosta', 'Liperi Joensuu lentoasema', 'Juuka Niemelä', 'Liperi Tuiskavanluoto', 'Joensuu Linnunlahti', 'Lieksa Lampela', 'Ilomantsi Pötsönvaara', 'Ilomantsi Mekrijärvi', 'Pietarsaari Kallan', 'Kokkola Tankar', 'Kruunupyy Kokkola-Pietarsaari lentoasema', 'Kalajoki Ulkokalla', 'Kokkola Santahaka', 'Toholampi Laitala', 'Ylivieska lentokenttä', 'Haapavesi Mustikkamäki', 'Pyhäjärvi Ojakylä', 'Kajaani lentoasema', 'Vieremä Kaarakkala', 'Nurmes Valtimo', 'Sotkamo Kuolaniemi', 'Kuhmo Kalliojoki', 'Raahe Nahkiainen', 'Hailuoto Keskikylä', 'Kemi I majakka', 'Hailuoto Marjaniemi', 'Raahe Lapaluoto satama', 'Oulu lentoasema', 'Siikajoki Ruukki', 'Oulu Vihreäsaari satama', 'Oulu Oulunsalo Pellonpää', 'Vaala Pelso', 'Pudasjärvi lentokenttä', 'Suomussalmi Pesiö', 'Puolanka Paljakka', 'Kemi Kemi-Tornio lentoasema', 'Kemi Ajos', 'Tornio Torppi', 'Ranua lentokenttä', 'Taivalkoski kirkonkylä', 'Kuusamo lentoasema', 'Kuusamo Kiutaköngäs', 'Kuusamo Rukatunturi', 'Kuusamo Juuma', 'Ylitornio Meltosjärvi', 'Pello kirkonkylä', 'Rovaniemi lentoasema', 'Rovaniemi rautatieasema', 'Sodankylä Tähtelä', 'Rovaniemi Apukka', 'Kemijärvi lentokenttä', 'Savukoski kirkonkylä', 'Pelkosenniemi Pyhätunturi', 'Salla kirkonkylä', 'Salla Naruska', 'Enontekiö lentoasema', 'Muonio Laukukero', 'Muonio Sammaltunturi', 'Kittilä Matorova', 'Kittilä lentoasema', 'Kittilä Kenttärova', 'Kittilä kirkonkylä', 'Kittilä Pokka', 'Sodankylä Lokka', 'Sodankylä Vuotso', 'Inari Saariselkä matkailukeskus', 'Inari Saariselkä Kaunispää', 'Inari Raja-Jooseppi', 'Salla Värriötunturi', 'Enontekiö Kilpisjärvi kyläkeskus', 'Enontekiö Kilpisjärvi Saana', 'Enontekiö Näkkälä', 'Inari Angeli Lintupuoliselkä', 'Inari Ivalo lentoasema', 'Utsjoki Kevo', 'Utsjoki Nuorgam', 'Inari Väylä', 'Inari Kaamanen', 'Inari Nellim', 'Inari Kirakkajärvi', 'Järvenpää Sorto', 'Mäntsälä Hirvihaara', 'Helsinki Vuosaari Käärmeniementie', 'Lahti Sopenkorpi', 'Sipoo Itätoukki', 'Rauma Pyynpää', 'Muonio kirkonkylä', 'Pyhtää lentokenttä', 'Kuusamo Välikangas', 'Sotkamo Tuhkakylä', 'Tervola Loue', 'Kajaani Petäisenniska', 'Utsjoki Kevo Kevojärvi', 'Inari Seitalaassa', 'Ilmajoki Seinäjoki lentoasema', 'Rovaniemi lentoasema AWOS', 'Jyväskylä lentoasema AWOS', 'Puumala kirkonkylä', 'Helsinki Vuosaari satama', 'Maarianhamina Länsisatama', 'Lumparland Långnäs satama', 'Tampere Tampella', 'Kittilä Lompolonvuoma', 'Kuusamo Ruka Talvijärvi', 'Espoo Nuuksio', 'Mikkeli Lentoasema AWOS', 'Espoo Tapiola']))
parameters = pd.Series(['temperature_2m', 'wind_speed_10min', 'wind_gust_10min', 'wind_direction_10min', 'relative_humidity', 'dew_point_temperature',
                'precipitation_amount_1h', 'precipitation_intensity_10min', 'snow_depth', 'pressure_at_sea_level', 'horizontal_visibility', 'cloud_amount', 'present_weather'])
# User input
station_id= st.selectbox(
            'Select station',
            stations)
parameter_id= st.selectbox(
            'Select parameter',
            parameters)
# If input exists
if station_id and parameter_id:
    query = {"station_name": station_id}
    exclude_dict ={}
    exclude_dict["_id"] = 0
    exclude_dict["station_name"] = 0
    exclude_dict["latitude"] = 0
    exclude_dict["longitude"] = 0
    # we need to exclude everything else but queried parameter
    for a_parameter in parameters:
        if a_parameter != parameter_id:
            exclude_dict[a_parameter]=0
    doc = col.find(query,exclude_dict) # query MondoDB

    df = pd.DataFrame(doc)
    print(df)
    st.header("Output")
    try: #if there are valid measurements
        graph1 = st.line_chart(data=df[parameter_id])
    except KeyError: #if not measurements available, display message
        st.text("No measurements available")
    