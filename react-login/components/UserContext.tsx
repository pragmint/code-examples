import React, { useContext, useState, Provider } from "react";

interface UserView {
  id: string;
  email: string;
  displayName: string;
}

interface UserContextValue {
  user: UserView | null;
  setUser: (user: UserView | null) => void;
  clear: () => void;
}

export const UserContext = React.createContext<UserContextValue>({
  user: null,
  setUser: (user: UserView | null) => {},
  clear: () => {},
});

type UserContextProviderProps = {
  children: React.ReactNode;
}

export const UserProvider = ({ children }: UserContextProviderProps) => {
  const [user, setUser] = useState<UserView | null>(null);
   
  return (
    <UserContext.Provider value={{
      user,
      setUser,
      clear: () => setUser(null),
    }}>
      {children}
    </UserContext.Provider>
  )
}

export const useUserContext = (): UserContextValue => {

  return useContext(UserContext);
};