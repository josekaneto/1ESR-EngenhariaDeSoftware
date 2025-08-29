import StatCard from "./StatCard";

export default function StatsGrid({stats}) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
      {stats.map((stat, index) => (
        <StatCard key={index} {...stat}/>
      ))}
    </div>
  );
}
