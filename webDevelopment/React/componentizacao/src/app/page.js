'use client'
import { useState } from "react";
import Header from "./components/Header";
import UserProfile from "./components/UserProfile";
import StatsGrid from "./components/StatsGrid";
import DataTable from "./components/DataTable";
import StatusBadge from "./components/StatusBadge";

const Dashboard = () => {
  const [user] = useState({
    name: 'João Silva',
    email: 'joao@email.com',
    avatar: 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.flaticon.com%2Fbr%2Ficone-gratis%2Favatar_3541871&psig=AOvVaw1q3AmPGKbDyI8_gkRp-oNo&ust=1756593600233000&source=images&cd=vfe&opi=89978449&ved=0CBUQjRxqFwoTCNCEg5-LsY8DFQAAAAAdAAAAABAE'
  });

  const [stats] = useState([
    { label: 'Vendas', value: 'R$ 12.500', change: '+15%', color: 'green' },
    { label: 'Usuários', value: '1.234', change: '+8%', color: 'blue' },
    { label: 'Pedidos', value: '89', change: '+23%', color: 'purple' },
    { label: 'Receita', value: 'R$ 45.200', change: '+12%', color: 'orange' }
  ]);

  const [recentOrders] = useState([
    { id: 1, customer: 'Maria Santos', amount: 'R$ 150', status: 'Entregue' },
    { id: 2, customer: 'Pedro Costa', amount: 'R$ 89', status: 'Em trânsito' },
    { id: 3, customer: 'Ana Lima', amount: 'R$ 320', status: 'Processando' }
  ]);

  const tableData = recentOrders.map((order) => ({
    ...order,
    id: `#${order.id}`,
    status: <StatusBadge status={order.status}/>
  }))

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <Header title="Dashboard">
        <UserProfile user={user}/>
      </Header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Stats Grid */}
        <StatsGrid stats={stats}/>

        {/* Recent Orders */}
        <DataTable 
        title="Pedidos Recentes" 
        columns={["ID", "Cliente", "Valor", "Status"]} 
        data={tableData}/>
      </main>
    </div>
  );
};

export default Dashboard