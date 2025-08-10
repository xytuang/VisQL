// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
import React, { useRef, useState } from 'react';

import { AppLayoutProps } from '@cloudscape-design/components/app-layout';
import Button from '@cloudscape-design/components/button';
import SpaceBetween from '@cloudscape-design/components/space-between';

import { Breadcrumbs, HelpPanelProvider, Notifications } from './commons';
import { CustomAppLayout } from './commons/common-components';
import { Content } from './components/content';
import { DashboardHeader, DashboardMainInfo } from './components/header';
import { DashboardSideNavigation } from './components/side-navigation';

import '@cloudscape-design/global-styles/dark-mode-utils.css';

export default function App() {
  const [toolsOpen, setToolsOpen] = useState(false);
  const [toolsContent, setToolsContent] = useState<React.ReactNode>(() => <DashboardMainInfo />);
  const [editorValue, setEditorValue] = useState('');
  const [jsonSpec, setJsonSpec] = useState<Record<string, any>>({})
  const appLayout = useRef<AppLayoutProps.Ref>(null);

  const handleToolsContentChange = (content: React.ReactNode) => {
    setToolsOpen(true);
    setToolsContent(content);
    appLayout.current?.focusToolsClose();
  };

  const handleEditorChange = (newEditorValue) => {
    setEditorValue(newEditorValue);
  }

  const runVisQL = async () => {
    const response = await fetch('http://localhost:4000/api/run-python', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ code: editorValue })
    });
    const newJsonSpec = await response.json();

    setJsonSpec(newJsonSpec['output'])
  }

  return (
    <HelpPanelProvider value={handleToolsContentChange}>
      <CustomAppLayout
        ref={appLayout}
        content={
          <SpaceBetween size="m">
            <DashboardHeader actions={<Button variant="primary" onClick={runVisQL}>Run code</Button>} />
            <Content onEditorChange={handleEditorChange} jsonSpec={jsonSpec}/>
          </SpaceBetween>
        }
        breadcrumbs={<Breadcrumbs items={[{ text: 'Dashboard', href: '#/' }]} />}
        navigation={<DashboardSideNavigation />}
        tools={toolsContent}
        toolsOpen={toolsOpen}
        onToolsChange={({ detail }) => setToolsOpen(detail.open)}
        notifications={<Notifications />}
      />
    </HelpPanelProvider>
  );
}
