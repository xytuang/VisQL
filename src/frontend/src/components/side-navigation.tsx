// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
import React, { useState } from 'react';

import Box from '@cloudscape-design/components/box';
import Link from '@cloudscape-design/components/link';
import Popover from '@cloudscape-design/components/popover';
import { SideNavigationProps } from '@cloudscape-design/components/side-navigation';

import { Navigation as CommonNavigation } from '../commons';

const navItems: SideNavigationProps['items'] = [
  { type: 'link', text: 'New editor', href: '#/' },
  {
    text: 'Bar Charts',
    type: 'section',
    defaultExpanded: true,
    items: [
      { type: 'link', text: 'Simple Bar Chart', href: '#/simple_bar_chart' },
      { type: 'link', text: 'Aggregate Bar Chart', href: '#/aggregate_bar_chart' },
      { type: 'link', text: 'Grouped Bar Chart', href: '#/grouped_bar_chart' },
    ],
  },
  {
    text: 'Histograms, Density Plots, and Dot Plots',
    type: 'section',
    defaultExpanded: false,
    items: [
      { type: 'link', text: 'Histogram', href: '#/histogram' },
      { type: 'link', text: 'Log-scaled histogram', href: '#/log_scaled_histogram' },
    ],
  },
  {
    text: 'Scatter & Strip Plots',
    type: 'section',
    defaultExpanded: false,
    items: [
      { type: 'link', text: 'Scatterplot', href: '#/scatterplot' },
      { type: 'link', text: 'Strip Plot', href: '#/strip_plot' },
    ],
  },
  {
    text: 'Line Charts',
    type: 'section',
    defaultExpanded: false,
    items: [
      { type: 'link', text: 'Line Chart', href: '#/line_chart' },
    ],
  },
  {
    text: 'Table-based Plots',
    type: 'section',
    defaultExpanded: false,
    items: [
      { type: 'link', text: 'Table Heatmap', href: '#/table_heatmap' },
    ],
  },
];

export function DashboardSideNavigation() {
  const onFollowHandler: SideNavigationProps['onFollow'] = event => {
    event.preventDefault();
  };

  return (
    <>
      <CommonNavigation items={navItems} activeHref="#/" onFollowHandler={onFollowHandler} />
    </>
  );
}