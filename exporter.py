
import csv
import json

class ParkExporter:

    def __init__(self, data):
        self.data = data

    def _aggregate(self):
        stats_map = {}

        for row in self.data:
            park = row["Branch"]
            rating = row["Rating"]
            loc = row["Reviewer_Location"]

            if park not in stats_map:
                stats_map[park] = {
                    "reviews": 0, "positive": 0,
                    "total_rating": 0, "countries": set()
                }
            stats_map[park]["reviews"] += 1
            stats_map[park]["total_rating"] += rating
            stats_map[park]["countries"].add(loc)
            if rating >= 4:
                stats_map[park]["positive"] += 1

        result = []
        for park, s in sorted(stats_map.items()):
            result.append({
                "park": park,
                "reviews": s["reviews"],
                "positive": s["positive"],
                "avg_score": round(s["total_rating"] / s["reviews"], 2),
                "countries": len(s["countries"]),
            })
        return result

    def export(self, fmt):
        stats = self._aggregate()
        filename = f"park_stats.{fmt}"

        exporters = {
            "txt": TxtExporter,
            "csv": CsvExporter,
            "json": JsonExporter,

        }

        if fmt not in exporters:
            raise ValueError(f"Unknown format: {fmt}")

        exporters[fmt].write(stats, filename)
        return filename

class TxtExporter:
    @staticmethod
    def write(stats, filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write("DISNEYLAND PARK STATISTICS\n")
            f.write("-" * 50 + "\n")
            for s in stats:
                f.write(f"park: {s['park']}\n")
                f.write(f"Total Reviews: {s['reviews']}\n")
                f.write(f"Positives (>=4): {s['positive']}\n")
                f.write(f"Average Score: {s['avg_score']}\n")
                f.write(f"Countries: {s['countries']}\n")
                f.write("\n")

class CsvExporter:
    @staticmethod
    def write(stats, filename):
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=[
                "park", "reviews", "positive", "avg_score", "countries"
            ])
            writer.writeheader()
            writer.writerows(stats)

class JsonExporter:
    @staticmethod
    def write(stats, filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(stats, f, indent=4)
