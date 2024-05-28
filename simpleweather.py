#Objective: This code is a function within a larger program that demonstrates interaction with an API and includes a user menu.
# It handles meteorological data from weather stations, performing sums and averages for each variable over defined periods

def operationweather(token, id, name, start_date, end_date, start_hour, end_hour, param, tipo, opcao):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    sum = 0.0
    count = 0

    while start_date <= end_date:
        delta = min(7, (end_date - start_date).days)
        temp_end_date = start_date + timedelta(days=delta)
        start = start_date + timedelta(hours=int(start_hour)) + timedelta(hours=3)
        end = temp_end_date + timedelta(hours=int(end_hour)) + timedelta(hours=3)

        if start_date == end_date:
            temp_end_date = start_date

        url = f" " #id
        params = {
            'start': start_date.strftime("%Y-%m-%d") + "T" + start_hour + ":00:00+0000",
            'end': temp_end_date.strftime("%Y-%m-%d") + "T" + end_hour + ":00:00+0000"
        }
        headers = {
            'Authorization': f'Bearer {token}'
        }

        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list) and data:
                data_to_sum = [
                    data[param] for data in data
                    if start <= datetime.strptime(data['started'], "%Y-%m-%dT%H:%M:%S+0000").replace(tzinfo=None) < end
                       and data.get(param) is not None]
                valid_data = [value for value in data_to_sum if value is not None]
                sum += sum(valid_data)
                count += len(valid_data)
        start_date = temp_end_date + timedelta(days=1)

    if tipo == 3 and count > 0 and opcao != 1: #different from accumulated solar radiation
        sum /= count

    if tipo == 3 and opcao == 1: #accumulated solar radiation
        sum /= 12
        days_in_period = ((end - start).days)+1
        sum = sum/days_in_period

    return round(sum, 1)