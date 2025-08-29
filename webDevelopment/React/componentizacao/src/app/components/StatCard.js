export default function StatCard({label, value, color, change}) {
  return (
    <div className="bg-white rounded-lg shadow p-6">
      <div className="flex items-center">
        <div className="flex-1">
          <p className="text-sm font-medium text-gray-600">{label}</p>
          <p className="text-2xl font-bold text-gray-900">{value}</p>
        </div>
        <div className={`text-sm font-medium text-${color}-600`}>
          {change}
        </div>
      </div>
    </div>
  );
}
