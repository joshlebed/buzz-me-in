import * as React from 'react';

interface myInterface {
  name: string;
}

const AdminPanel: React.FunctionComponent<myInterface> = (props: myInterface) => {
  const { name } = props;
  return <h1>Hola, {name}! </h1>;
};

export default AdminPanel;
