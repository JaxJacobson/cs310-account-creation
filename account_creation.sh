creation()
    {
    read -p "Enter your First and Last Name: " name
    username="${name// /-}"
    read -p "Are you a [A]User, [B]AV Tech, or [C]Admin: " role
    }

read -p "Your username is $username, and you are a $role. Is this correct? (Y/N): " confirmation
if [[ "$confirmation" =~ ^[Yy]$ ]]; then
    echo "Creating your account..."
else
    creation()

