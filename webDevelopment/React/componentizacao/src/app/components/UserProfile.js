const UserProfile = ({ user }) => {
  return (
    <div className="flex items-center space-x-4">
      <span className="text-gray-700">{user.name}</span>
      <img
        className="w-10 h-10 rounded-full"
        src={user.avatar}
        alt={user.name}
      />
    </div>
  );
};

export default UserProfile
