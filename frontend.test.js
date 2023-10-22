/**
 * @file This file adds unit tests for the functions in frontend.js.
 * It ensures all functions behave as expected under various conditions.
 */

import * as frontend from './frontend.js';

// Mock fetch global function for testing
global.fetch = jest.fn(() =>
  Promise.resolve({
    json: () => Promise.resolve({}),
    ok: true
  })
);

describe('Frontend functions', () => {
  beforeEach(() => {
    fetch.mockClear();
  });

  test('element1Action makes a fetch request', async () => {
    await frontend.element1Action();
    expect(fetch).toHaveBeenCalledWith('/api/element1');
  });

  test('element2Action makes a fetch request', async () => {
    await frontend.element2Action();
    expect(fetch).toHaveBeenCalledWith('/api/element2');
  });

  test('newFeatureAction makes a fetch request', async () => {
    await frontend.newFeatureAction();
    expect(fetch).toHaveBeenCalledWith('/api/new_feature');
  });

  test('anotherNewFeatureAction makes a fetch request', async () => {
    await frontend.anotherNewFeatureAction();
    expect(fetch).toHaveBeenCalledWith('/api/another_new_feature');
  });
});