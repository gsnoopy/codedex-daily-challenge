def pick_voucher(vouchers, delays, max_wait):
    result = []

    for voucher, delay in zip(vouchers, delays):
        if delay > max_wait:
            result.append(None)
        else:
            per_hour = voucher / delay
            result.append(per_hour)

    if all(x is None for x in result):
        return -1

    max_value = max(x for x in result if x is not None)
    return result.index(max_value)