import * as React from 'react';
import { AppContainer, PageContainer } from './SharedComponents';
import UnlockButtonForm from './UnlockButtonForm';

const App = () => (
  <PageContainer>
    <AppContainer>
      {/* TODO: add react router */}
      <UnlockButtonForm />
    </AppContainer>
  </PageContainer>
);

export default App;
