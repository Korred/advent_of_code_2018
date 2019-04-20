license_file = list(map(int, open('input.txt').readline().strip().split()))


def parse_license(data):
    children_cnt, metadata_cnt = data[:2]
    data = data[2:]
    metadata_sum = 0

    for i in range(children_cnt):
        meta_sum, data = parse_license(data)
        metadata_sum += meta_sum

    metadata_sum += sum(data[:metadata_cnt])
    
    return (metadata_sum, data[metadata_cnt:])

print("Sum of all metadata entries:", parse_license(license_file)[0])





