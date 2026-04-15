def select_parcels(parcels, capacity):
    # Sort by value-to-weight ratio
    parcels = sorted(parcels, key=lambda x: x['value']/x['weight'], reverse=True)

    selected = []
    total_weight = 0

    for parcel in parcels:
        if total_weight + parcel['weight'] <= capacity:
            selected.append(parcel)
            total_weight += parcel['weight']

    return selected