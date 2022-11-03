def sort(ds, data: str, d_id: str) -> list:
    sorted_list = [[] for _ in range(15)]

    try:
        for x in ds:
            if isinstance(x, dict):
                for i, d in enumerate(x.values()):
                    sorted_list[int(d[d_id])].append(d[data])
    except IndexError:
        traceback.format_exc()
    except KeyError:
        traceback.format_exc()

    return sorted_list