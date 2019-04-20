license_file = list(map(int, open('input.txt').readline().strip().split()))


def parse_license(data):
    children_cnt, metadata_cnt = data[:2]
    data = data[2:]
    metadata_sum = 0
    values = []

    for i in range(children_cnt):
        meta_sum, data, value = parse_license(data)
        metadata_sum += meta_sum
        values.append(value)

    metadata_sum += sum(data[:metadata_cnt])

    if children_cnt == 0:
        return (metadata_sum, data[metadata_cnt:], sum(data[:metadata_cnt]))
    else:
        return (metadata_sum, data[metadata_cnt:], sum(values[s - 1] for s in data[:metadata_cnt] if s <= len(values) and s > 0))


print("Root value:", parse_license(license_file)[2])
