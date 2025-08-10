// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
import React from 'react';

import Header from '@cloudscape-design/components/header';
import HelpPanel from '@cloudscape-design/components/help-panel';

import { ExternalLinkGroup, InfoLink, useHelpPanel } from '../commons';

export function DashboardMainInfo() {
  return (
    <HelpPanel
      header={<h2>Service</h2>}
      footer={
        <ExternalLinkGroup
          items={[
            { href: '#', text: 'Paper' },
            { href: '#', text: 'Github' },
            { href: '#', text: 'Documentation' },
            { href: '#', text: 'API Reference' },

          ]}
        />
      }
    >
      <p>
        VisQL is an interactive web-based tool that leverages a novel visualization formalism
        designed to handle multi-table relational data. Unlike traditional visualization libraries
        that require manual data transformation, VisQL allows users to directly query and visualize
        complex database schemas. By mapping database constraints—such as schemas, types, and foreign keys—to visual representations,
        VisQL ensures that visualizations are both expressive and semantically accurate,
        providing a faithful representation of the underlying data.
      </p>
    </HelpPanel>
  );
}

export function DashboardHeader({ actions }: { actions: React.ReactNode }) {
  const loadHelpPanelContent = useHelpPanel();
  return (
    <Header
      variant="h1"
      info={<InfoLink onFollow={() => loadHelpPanelContent(<DashboardMainInfo />)} />}
      actions={actions}
    >
      VisQL
    </Header>
  );
}